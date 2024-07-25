# Determine number of datasets
import json


def format_data(model_response):
    # prep data into key value pairs
    instruction = "You are a technology analyst that analyzes text and summarizes it into easy to read language"
    response = json.loads(model_response)
    data = {
        "instruction": instruction
    }
    data.update(response)
    return data


def save_data(dataset):
    # store full dictionary into json file
    file_path = "../data/dataset.json"

    with open(file_path, "w") as file:
        json.dump(dataset, file, indent=4)
