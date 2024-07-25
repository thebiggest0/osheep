# Determine number of datasets

def create_dataset_format(prompt, output):
    # prep data into key value pairs
    instruction = "You are a technology analyst that analyzes text and summarizes it into easy to read language"
    user_input = prompt
    model_output = output
    data = {
        "instruction": instruction,
        "input": user_input,
        "output": model_output
    }
    return data


def make_data():
    # access model
    # based off paragraph length ask it to generate number of input and outputs to summarize text
    # format using create_dataset_format
    # store each into a growing dictionary
    pass


def save_data():
    # store full dictionary into json file
    pass