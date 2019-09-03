from cmake_analyzer.core import module_base


class TestCheckerCustomModule(module_base.SingleFileChecker):
    def process_file(self, ast, root_directory, filename):
        pass
