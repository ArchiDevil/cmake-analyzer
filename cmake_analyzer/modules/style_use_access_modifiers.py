import os

from cmake_analyzer.core import module_base
from cmake_analyzer.core.reporter_base import create_diagnostic


class AccessModifiersChecker(module_base.SingleFileChecker):
    error = 'Do not use target_link_libraries command without access specifiers.'

    def process_file(self, ast, root_directory, filename):
        diags = []

        for node in ast:
            if 'command' not in node.keys():
                continue

            if node['command']['name'].lower() == 'target_link_libraries':
                found = False
                for arg_node in node['command']['args']:
                    if not isinstance(arg_node, dict):
                        continue

                    if arg_node['arg'][0] in ['PUBLIC', 'PRIVATE', 'INTERFACE']:
                        found = True

                if not found:
                    diag = create_diagnostic(
                        node, AccessModifiersChecker.error)
                    diags.append(diag)

        return diags