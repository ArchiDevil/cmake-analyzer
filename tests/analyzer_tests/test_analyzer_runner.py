import builtins
import os

from cmake_analyzer import analyzer

def test_analyzer_can_list_checks():
    class Checker(object):
        result = False
        print_calls = []

        @staticmethod
        def printer(*args):
            Checker.print_calls.append(str(args))
            Checker.result = True

    old_print = builtins.print
    builtins.print = Checker.printer
    analyzer.main(['fake', '--list-checks'])
    builtins.print = old_print
    assert Checker.result
    assert Checker.print_calls


def test_analyzer_can_be_run():
    class Checker(object):
        result = False
        print_calls = []

        @staticmethod
        def printer(*args):
            Checker.print_calls.append(str(args))
            Checker.result = True

    old_print = builtins.print
    builtins.print = Checker.printer
    analyzer.main(['fake', '--exclude', '*exclude_me*', '-p', os.path.join(os.path.dirname(__file__), 'sample_project')])
    builtins.print = old_print
    assert Checker.result
    assert Checker.print_calls
