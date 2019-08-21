import argparse
import tatsu
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    
    simplified_grammar = open('simple_grammar.ebnf', 'r').read()
    content = open(args.path).read()
    ast = tatsu.parse(simplified_grammar, content)
    code = tatsu.to_python_sourcecode(simplified_grammar)
    open('model.py', 'w').write(code)
    print(json.dumps(ast, indent=4))

if __name__ == '__main__':
    main()
