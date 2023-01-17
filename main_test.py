import os
import openai
import glob
import ast

openai.api_key = "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"
# script_path = '/Users/monolite/Documents/GitHub/Meshroom/meshroom/core/cgroup.py'


def sum(a, b):
    return a+b


def main():
    # List all the files in the directory
    # folder_path = 'algorithms/matrix'
    folder_path = '/Users/monolite/Documents/GitHub/growth-estimation/Server'
    # files = os.listdir(folder_path)
    os.chdir(folder_path)
    # Iterate over the list of file names
    for i, file in enumerate(glob.glob('**/*.py', recursive=True)):
        print(file)
        if not os.path.isfile(os.path.join(folder_path, file.replace('py', 'md'))) and file.endswith('.py'):
            # Open the file
            with open(os.path.join(folder_path, file), 'r') as f:
                # Read the contents of the file
                contents = f.read()
                try:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"create .md file for this script with code snippets:\n`{contents}`",
                        temperature=0.7,
                        max_tokens=15000,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    print(response["choices"][0]["text"])
                    with open(os.path.join(folder_path, file.replace('py', 'md')), 'w') as output_file:
                        output_file.write(response["choices"][0]["text"])
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()
    # file_lines = source_code.splitlines()
    # # Parse the source code into an AST
    # tree = ast.parse(source_code)
    #
    # # Iterate over the AST nodes
    # for node in ast.walk(tree):
    #     # Check if the node is a FunctionDef node (i.e., a function definition)
    #     if isinstance(node, ast.FunctionDef):
    #         # # Print the function name
    #         # print(node.name)
    #         # print('--------------')
    #         # print('\n'.join(file_lines[node.lineno-1: node.end_lineno]))
    #         #
    #         # newline = '\n'
    #         # # response = openai.Completion.create(
    #         # #     model="code-davinci-002",
    #         # #     prompt=f"# Python 3 \n{newline.join(file_lines[node.lineno-1: node.end_lineno])}\n# Explanation of what the code does\n\n#",
    #         # #     temperature=0,
    #         # #     max_tokens=64,
    #         # #     top_p=1.0,
    #         # #     frequency_penalty=0.0,
    #         # #     presence_penalty=0.0
    #         # # )
    #
    #         print('--------------')
