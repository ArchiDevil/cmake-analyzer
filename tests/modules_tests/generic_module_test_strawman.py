import os

from cmake_analyzer.core import parser


class GenericModuleTestGenerator:
    def __init__(self, module_globals, test_class, test_file, test_lines):
        def partial():
            p = parser.CMakeParser('cmake_analyzer/static/simple_grammar.ebnf')
            ast = p.parse_file(os.path.join(test_file))
            diags = test_class.process_file(ast,
                                            '/some/directory/',
                                            'CMakeLists.txt')
            assert len(diags) == len(test_lines)
            for i, diag in enumerate(diags):
                assert test_lines[i] == diag.line

        module_globals['test_something'] = partial
