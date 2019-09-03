class SimpleReporter:
    @staticmethod
    def report(iterable):
        for diag in iterable:
            print('{}:{} - {}'.format(diag.file, diag.line, diag.message))

    @staticmethod
    def end():
        pass
