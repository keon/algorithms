import ast
import glob
import os
import json


def find_docstrings(node):
    docstrings = []
    if isinstance(node, ast.Module):
        for child in node.body:
            docstrings.extend(find_docstrings(child))
    elif isinstance(node, ast.FunctionDef):
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
            docstrings.append(node.body[0])
        for child in node.body[1:]:
            docstrings.extend(find_docstrings(child))
    elif isinstance(node, ast.ClassDef):
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
            docstrings.append(node.body[0])
        for child in node.body[1:]:
            docstrings.extend(find_docstrings(child))
    return docstrings


def remove_docstrings(node):
    if isinstance(node, ast.Module):
        for child in node.body:
            remove_docstrings(child)
    elif isinstance(node, ast.FunctionDef):
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
            node.body.pop(0)
        for child in node.body:
            remove_docstrings(child)


def get_functions(filename, remove_docstring=True):
    with open(filename, 'r') as f:
        # parse the source code into an AST
        root = ast.parse(f.read())

    # create a list to store the functions
    output_functions = []

    # iterate over the nodes in the AST
    for node in ast.walk(root):
        # if this is a FunctionDef node, add it to the list
        if isinstance(node, ast.FunctionDef):
            if remove_docstring:
                remove_docstrings(node)
            output_functions.append(ast.unparse(node))

    return output_functions


def get_all_files(folder_path):
    os.chdir(folder_path)
    return [os.path.join(folder_path, f) for f in glob.glob('**/*.py', recursive=True)]




def export_json_from_functions(functions_list, f_name):
    with open(f_name, 'w') as file:
        json.dump(functions_list, file, indent=2)


if __name__ == '__main__':
    # test the function with a sample Python file
    folders_path = '/Users/monolite/Documents/GitHub/Meshroom'
    code_files = get_all_files(folders_path)
    functions = []
    for code_file in code_files:
        functions.extend(get_functions(code_file))

    export_json_from_functions(functions, '/Users/monolite/Documents/GitHub/algorithms/meshroom_funcs.json')
    # print(functions)
    # functions = get_functions('../algorithms/arrays/delete_nth.py')
    # print(functions)
