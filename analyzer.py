import argparse
import tatsu
import json
import sys

from core import *


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-c', '--checks',
                           help='enable checks in the following format: style* legacy*',
                           default=['*'],
                           nargs='+',
                           type=str)
    argparser.add_argument('-v', '--verbose',
                           help='enable verbose logging for large projects',
                           action='store_true')

    me_group = argparser.add_mutually_exclusive_group(required=True)
    me_group.add_argument('-p', '--path',
                          help='path to start check from',
                          type=str)
    me_group.add_argument('-lc', '--list-checks',
                          help='list all available checks',
                          action='store_true')

    args = argparser.parse_args()

    if args.list_checks:
        loader = modules_loader.ModulesLoader('modules', args.checks)
        for module in loader.loaded_modules:
            print(module.__name__)
        exit()

    loader = modules_loader.ModulesLoader('modules')
    file_parser = parser.CMakeParser('core/simple_grammar.ebnf')
    project_traverser = traverser.Traverser(file_parser,
                                            checkers=loader.loaded_checkers,
                                            verbose=True if args.verbose else False)

    project_traverser.traverse(args.path)


if __name__ == '__main__':
    main()
