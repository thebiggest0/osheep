"""
Determine number of datasets
"""

import json
import connect_model


def format_data(model_response):
    # prep data into key value pairs
    input = ""
    model_response = json.loads(model_response)
    for data in model_response:
        data.update({"input": input})
    return model_response


def read_data(save_path):
    with open(save_path, "r") as file:
        data = json.load(file)
    return data


def save_data(dataset, file_path, save_path):
    # store full dictionary into json file
    data = read_data(save_path)
    data.extend(dataset)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def confirm_data_format(model, dataset):
    # # model_prompt = f"## Check if the text under ### Content is a python list of dictionaries with keys: instruction, response \n ### Content: '{dataset} \n ## if there is other text outside of the python list, remove it and return only the list of dictionaries"
    # model_prompt = f"Validate if the 'Input string' contains a Python list of dictionaries. Only respond with the list containing the dictionary, do not add any other text or description. If there is any text outside the list, remove it and return only the list containing dictionaries as a string. Input string: {dataset}"
    # return connect_model.request_model(model, model_prompt)

    while dataset[0] != "[":
        dataset = dataset[1:]
    while dataset[-1] != "]":
        dataset = dataset[:-1]


def create_input(model, dataset, content):
    dataset = json.loads(dataset)
    for data in dataset:
        model_prompt = f"#Based on the text in the ##Content and the instruction: {data['instruction']} and the response {data['response']}, generate the corresponding input. ##Content: {content}"
        generated_input = connect_model.request_model(model, model_prompt)
        data["input"] = generated_input.strip()
    return dataset
