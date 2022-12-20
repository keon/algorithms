import os
import openai
import ast

openai.api_key = "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"
# script_path = '/Users/monolite/Documents/GitHub/Meshroom/meshroom/core/cgroup.py'


# List all the files in the directory
folder_path = 'algorithms/matrix'
files = os.listdir(folder_path)

# Iterate over the list of file names
for file in files:
    if file.endswith('.py'):
        # Open the file
        with open(os.path.join(folder_path, file), 'r') as f:
            # Read the contents of the file
            contents = f.read()
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"create .md file for this script with code snippets:\n`{contents}`",
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response["choices"][0]["text"])
            with open(file.replace('py', 'md'), 'w') as output_file:
                output_file.write(response["choices"][0]["text"])

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
