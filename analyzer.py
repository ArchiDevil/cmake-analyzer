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

    me_group_action = argparser.add_mutually_exclusive_group(required=True)
    me_group_action.add_argument('-p', '--path',
                                 help='path to start check from',
                                 type=str)
    me_group_action.add_argument('--list-checks',
                                 help='list all available checks',
                                 action='store_true')

    me_group_including_excluding = argparser.add_mutually_exclusive_group()
    me_group_including_excluding.add_argument('--exclude',
                                              help='filter out files by mask',
                                              default=None,
                                              nargs='+',
                                              type=str)
    me_group_including_excluding.add_argument('--include',
                                              help='include only files by mask',
                                              default=['*'],
                                              nargs='+',
                                              type=str)

    args = argparser.parse_args()

    include_filters = args.include
    exclude_filters = args.exclude

    if exclude_filters:
        include_filters = None

    if args.list_checks:
        loader = modules_loader.ModulesLoader('modules', args.checks)
        for module in loader.loaded_modules:
            print(module.__name__)
        exit()

    loader = modules_loader.ModulesLoader('modules')
    file_parser = parser.CMakeParser('core/simple_grammar.ebnf')
    project_traverser = traverser.Traverser(file_parser,
                                            checkers=loader.loaded_checkers,
                                            include_filters=include_filters,
                                            exclude_filters=exclude_filters,
                                            verbose=True if args.verbose else False)

    project_traverser.traverse(args.path)


if __name__ == '__main__':
    main()
