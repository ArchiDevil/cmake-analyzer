from cmake_analyzer.core import module_base


class TestCheckerProcessFile(module_base.SingleFileChecker):
    def process_file(self, ast, root_directory, filename):
        pass


class TestCheckerMissedProcess(module_base.SingleFileChecker):
    pass


class InvalidCheckerInheritance(object):
    def process_file(self, ast, root_directory, filename):
        pass


class TestCheckerProcessDir(module_base.SingleFileChecker):
    def process_directory(self, root_directory, dirname):
        pass


class TestCheckerEndProcessing(module_base.SingleFileChecker):
    def end_processing(self):
        pass


class TestCheckerFakeEndProcessing(module_base.SingleFileChecker):
    end_processing = False
