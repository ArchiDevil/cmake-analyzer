from cmake_analyzer.core import module_base
from cmake_analyzer.core.reporter_base import create_diagnostic


class VersionUsageChecker(module_base.SingleFileChecker):
    minimum_required_error = 'Do not use cmake_minimum_required(...) command in any of underlying cmake files. Use it only in root CMakeLists.txt'
    policy_error = 'Do not use cmake_policy(VERSION ...) in any of underlying cmake files. Use it only in root CMakeLists.txt'

    @staticmethod
    def __is_root_cmake(filename):
        return filename == 'CMakeLists.txt'

    @staticmethod
    def __process_minimum_required(command_node):
        return [create_diagnostic(command_node, VersionUsageChecker.minimum_required_error)]

    @staticmethod
    def __process_policy(command_node):
        if command_node['args'][0]['arg'][0].upper() != 'VERSION':
            return []
        return [create_diagnostic(command_node, VersionUsageChecker.policy_error)]

    def process_file(self, ast, root_directory, filename):
        diags = []

        if VersionUsageChecker.__is_root_cmake(filename):
            return []

        for node in ast:
            if 'command' not in node.keys():
                continue

            if node['command']['name'].lower() == 'cmake_minimum_required':
                diags += self.__process_minimum_required(node['command'])

            if node['command']['name'].lower() == 'cmake_policy':
                diags += self.__process_policy(node['command'])

        return diags
