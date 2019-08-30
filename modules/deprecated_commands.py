import os

from core import module_base
from core.reporter_base import create_diagnostic_from_node

class DeprecatedCommandsChecker(module_base.SingleFileChecker):
    deprecated_commands = ['build_name',
                           'exec_program',
                           'export_library_dependencies',
                           'install_files',
                           'install_programs',
                           'install_targets',
                           'load_command',
                           'make_directory',
                           'output_required_files',
                           'qt_wrap_cpp',
                           'qt_wrap_ui',
                           'remove',
                           'subdir_depends',
                           'subdirs',
                           'use_mangled_mesa',
                           'utility_source',
                           'variable_requires',
                           'write_file']

    def process_file(self, ast, root_directory, filename):
        diags = []

        for node in ast:
            if not 'command' in node.keys():
                continue

            command_name = node['command']['name'].lower()

            if command_name in DeprecatedCommandsChecker.deprecated_commands:
                diag = create_diagnostic_from_node(node,
                                                   os.path.join(
                                                       root_directory, filename),
                                                   "Command {} is deprecated, consider removing it.".format(command_name))
                diags.append(diag)

        return diags
