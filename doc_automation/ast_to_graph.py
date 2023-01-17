import sys


import ast

def main():
    ast.parse()
    lexer = ASTLexer(sys.stdin)
    parser = ASTParser(lexer)

    root = parser.parse().value
    export_ast_digraph(root)

id_counter = 0


class AbstractSymbol:
    pass


def export_ast_digraph(root):
    global id_counter
    node_id = str(id_counter)
    id_counter += 1
    label = []
    root_class = type(root)
    label.append(root_class.__name__)

    while root_class is not None:
        for field in root_class.__dict__:
            if not field.startswith('__'):
                field_value = getattr(root, field)
                if isinstance(field_value, AbstractSymbol):
                    label.append(f'{field}: {field_value}')
                elif isinstance(field_value, ListNode):
                    child_it = Utilities.iterable(field_value)
                    counter = 0
                    for child in child_it:
                        child_id = export_ast_digraph(child)
                        print(f'{node_id} -> {child_id} [label="{field}_{counter}"];')
                        counter += 1
                elif isinstance(field_value, TreeNode):
                    child_id = export_ast_digraph(field_value)
                    print(f'{node_id} -> {child_id} [label="{field}"];')

        root_class = root_class.__base__

    print(f'{node_id}[label="{label}"];')
    return node_id

if __name__ == '__main__':
    main()
