from core import module_base


class TestCheckerValid(module_base.SingleFileChecker):
    def process(self, ast, root_directory, filename):
        pass


class TestCheckerMissedProcess(module_base.SingleFileChecker):
    pass

class InvalidCheckerInheritance(object):
    def process(self, ast, root_directory, filename):
        pass
