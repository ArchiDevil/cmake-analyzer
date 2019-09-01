from core import reporter_base


class SimpleReporter(object):
    def report(self, iterable):
        for diag in iterable:
            print('{}:{} - {}'.format(diag.file, diag.line, diag.message))

    def end(self):
        pass
