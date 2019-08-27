from enum import Enum
import os
import re

from .parser import CMakeParser
from reporters import simple


class Mode(Enum):
    GLOBAL = 0


class Traverser(object):
    def __init__(self, parser: CMakeParser, checkers=[], reporters=[simple.SimpleReporter()], mode=Mode.GLOBAL, verbose=False):
        if not parser or not isinstance(parser, CMakeParser):
            raise TypeError('parser argument must be of type CMakeParser()')

        self.mode = mode
        self.parser = parser
        self.checkers = checkers
        self.reporters = reporters
        self.verbose = verbose

    def traverse(self, path):
        root_cmake = None
        root_path = None
        for file in os.listdir(path):
            if file == 'CMakeLists.txt':
                root_cmake = os.path.join(os.path.abspath(path), file)
                root_path = os.path.dirname(root_cmake)

        if not root_cmake:
            raise RuntimeError(
                'CMakeLists.txt has not been found in {}'.format(path))

        for dirname, _, filenames in os.walk(path):
            for filename in filenames:
                if not re.findall(r'(CMakeLists\.txt|.*\.cmake)', filename):
                    continue

                if self.verbose:
                    print('Processing {}'.format(
                        os.path.join(dirname, filename)))

                diagnostics = []
                ast = self.parser.parse_file(os.path.join(dirname, filename))

                for checker in self.checkers:
                    results = checker.process(ast, root_path, os.path.relpath(
                        os.path.join(dirname, filename), root_path))
                    diagnostics += results

                for reporter in self.reporters:
                    reporter.report(diagnostics)

        for reporter in self.reporters:
            reporter.end()
