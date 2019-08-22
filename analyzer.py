import argparse
import tatsu
import json
import sys

from core import *

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', type=str)
    args = argparser.parse_args()
    
    traverser = parser.Parser('core/simple_grammar.ebnf')
    try:
        ast = traverser.parse_file(args.path)
    except Exception as e:
        print(e)
        exit()

    for element in ast:
        if 'command' in element:
            command = element['command']
            print('{} #{}'.format(command['name'], command['parseinfo'].line))

if __name__ == '__main__':
    main()
