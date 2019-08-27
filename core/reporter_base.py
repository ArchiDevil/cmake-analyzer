from collections import namedtuple

Diagnostic = namedtuple('Diagnostic', 'file line message')

def create_diagnostic_from_node(node, file, message):
    parse_info = node['parseinfo']
    return Diagnostic(file, parse_info.line + 1, message)
