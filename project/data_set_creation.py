"""
Determine number of datasets
"""

import json


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
