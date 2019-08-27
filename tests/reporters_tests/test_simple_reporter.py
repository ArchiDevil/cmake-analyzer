from collections import namedtuple
import builtins

Parseinfo = namedtuple('Parseinfo', 'line')

from core import reporter_base
from reporters import simple

def test_can_create_diagnostic_from_node():
    node = {'parseinfo': Parseinfo(21)}
    file = 'test'
    message = 'error!'
    diag = reporter_base.create_diagnostic_from_node(node, file, message)

    assert diag.line == node['parseinfo'].line + 1
    assert diag.file == file
    assert diag.message == message

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
    diag = reporter_base.create_diagnostic_from_node(node, file, message)
    builtins.print = Checker.printer

    reporter.report([diag])
    assert Checker.result

def test_simple_reporter_ends_without_errors():
    reporter = simple.SimpleReporter()
    reporter.end()
