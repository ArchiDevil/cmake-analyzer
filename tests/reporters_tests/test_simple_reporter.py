from reporters import simple
from core import reporter_base
from collections import namedtuple
import builtins

Parseinfo = namedtuple('Parseinfo', 'line')


def test_can_create_diagnostic_from_node():
    node = {'parseinfo': Parseinfo(21)}
    file = 'test'
    message = 'error!'
    module = 'test_module'
    simple_diag = reporter_base.create_diagnostic(node, message)
    diag = reporter_base.create_full_diagnostic(simple_diag, file, module)

    assert diag.line == node['parseinfo'].line + 1
    assert diag.file == file
    assert diag.message == message
    assert diag.module == module


def test_simple_reporter_reports_in_console():
    class Checker(object):
        result = False

        @staticmethod
        def printer(*args):
            Checker.result = True

    reporter = simple.SimpleReporter()
    node = {'parseinfo': Parseinfo(21)}
    file = 'test'
    message = 'error!'
    module = 'test_module'
    simple_diag = reporter_base.create_diagnostic(node, message)
    diag = reporter_base.create_full_diagnostic(simple_diag, file, module)
    builtins.print = Checker.printer

    reporter.report([diag])
    assert Checker.result


def test_simple_reporter_ends_without_errors():
    reporter = simple.SimpleReporter()
    reporter.end()
