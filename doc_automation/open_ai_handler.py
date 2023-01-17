import inspect
import json
import openai
from tqdm import tqdm
import random
import time

from doc_automation.decorators import rate_limit

openai.api_key = "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"


def get_function_docs(input_functions_json, output_jsonl_path, limit_request_from_file=None):
    prompt = 'give me the docstring for this function:'
    out_train_json = []

    func_list = read_json_file(input_functions_json)
    random.shuffle(func_list)

    for i, func_txt in tqdm(enumerate(func_list)):
        if limit_request_from_file is not None and not i < limit_request_from_file:
            break
        openai_res = request_openapi_prompt(prompt, func_txt)
        if openai_res is not None:
            # out_train_json.append({
            #     'prompt': f'{func_txt}\n##############\nEND_FUNC\n##############\n',
            #     'completion': openai_res
            # })
            append_to_file({
                'prompt': f'{func_txt}\n##############\nEND_FUNC\n##############\n',
                'completion': openai_res
            }, output_jsonl_path)
        else:
            print('is none', func_txt)
        print('done', i)

    # write_jsonl_file(out_train_json, output_jsonl_path)


@rate_limit(60)
def request_openapi_prompt(prompt, func_text):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{prompt}\n`\n{func_text}\n`",
            temperature=0.7,
            max_tokens=1459,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"]

    except Exception as e:
        print(e)


def read_json_file(input_functions_json):
    # Open the JSON file
    with open(input_functions_json, 'r') as f:
        # Load the contents of the file into a Python variable
        func_list = json.load(f)
    return func_list


def write_jsonl_file(json_list_object, output_jsonl_path):
    with open(output_jsonl_path, 'w') as f:
        # Iterate over the list and write each element to the file
        for item in json_list_object:
            json.dump(item, f)
            # Add a newline character after each element
            f.write('\n')


def append_to_file(data_line, output_file):
    with open(output_file, 'a') as f:
        json.dump(data_line, f)
        f.write('\n')


def fix_jsonl_file(file_path):
    func_list = []
    # Open the JSONL file
    with open(file_path, 'r') as f:
        # Iterate over the lines in the file
        for line in f:
            # Load the JSON data from each line
            func_list.append(json.loads(line))
    for func in func_list:
        if not func['completion']:
            func_list.remove(func)
            print('')

    print(func_list)


def get_func_flowchart_test():
    func_list = read_json_file('out.json')
    test_func = func_list[52]
    res = request_openapi_prompt('give me control graph for this function in dot language:', test_func)
    print('')


def create_control_graph(func):
    lines = inspect.getsource(func).split('\n')
    nodes = []
    edges = []
    for i, line in enumerate(lines):
        if line.startswith('if'):
            nodes.append(line)
            if ':' in lines[i+1]:
                edges.append((line, lines[i+1]))
            else:
                edges.append((line, lines[i+2]))
    graph = 'digraph G {\n'
    for node in nodes:
        graph += f'    "{node}" [shape=diamond];\n'
    for src, dest in edges:
        graph += f'    "{src}" -> "{dest}";\n'
    graph += '}'
    return graph


if __name__ == '__main__':
    print(create_control_graph(fix_jsonl_file))

    # get_function_docs('meshroom_funcs.json', 'meshroom_funcs_training.jsonl')
    # get_func_flowchart_test()
# fix_jsonl_file('training_data.jsonl')
