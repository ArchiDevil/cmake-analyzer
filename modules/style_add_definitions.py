import os

from core import module_base
from core.reporter_base import create_diagnostic


class AddDefinitionsFinder(module_base.SingleFileChecker):
    error = 'Do not use add_definitions() command. It was superseeded by add_compile_definitions/include_directories/add_compile_options. Use these commands instead.'

    def process_file(self, ast, root_directory, filename):
        diags = []

        for node in ast:
            if 'command' not in node.keys():
                continue

            if node['command']['name'].lower() == 'add_definitions':
                diags.append(create_diagnostic(
                    node, AddDefinitionsFinder.error))

        return diags
