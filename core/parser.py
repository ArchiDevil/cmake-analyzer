import tatsu
import tatsu.model

class Parser(object):
    def __init__(self, grammar_file):
        with open(grammar_file, 'r') as fp:
            grammar = fp.read()
        self.model = tatsu.compile(grammar, name='CMake')
        
    def parse_file(self, file):
        with open(file, 'r') as fp:
            content = fp.read()
            
        ast = self.model.parse(content)
        return ast
    
    def save_model(self, out_file_source_code):
        python_sourcecode = tatsu.to_python_sourcecode(self.model, filename=out_file_source_code)
        with open(out_file_source_code, 'w') as fp:
            fp.write(python_sourcecode)
