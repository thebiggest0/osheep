import connect_model
import data_set_creation
import process_text


def main():
    paragraphs = process_text.break_down_text()
    # dataset = []
    # for paragraph in paragraphs:
    count = paragraphs[1] // 120
    if count == 0:
        count = 1

    model_mistral = "mistral"
    prompt_mistral = f'#based on the content, summarize the paragraph and return only a python list which contains 5 different dictionaries of key value pairs covering key points of the paragraph. Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "target output for the given prompt, per the instructions and context provided"}} ## content: "{paragraphs[0]}"'
    file_path_mistral = "../data/dataset.json"
    save_path_mistral = "../data/dataset.json"
    mistral = False

    model = "gemma2"
    prompt = f'#based on the ##content, summarize the paragraph and return only a python list (nothing extra) which contains 5 different dictionaries of key value pairs covering key points of the paragraph see ##Example for dictionary key value pair template. ##Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "target output for the given prompt, per the instructions and context provided"}} ## content: "{paragraphs[0]}"'
    file_path = "../data/dataset_gemma.json"
    save_path = "../data/dataset_gemma.json"
    # gemma = False

    if mistral:
        response = connect_model.request_model(model_mistral, prompt_mistral)
        print(response)

        cleaned_dataset = data_set_creation.format_data(response)
        print(cleaned_dataset)

        data_set_creation.save_data(data_set_creation.format_data(response), file_path_mistral, save_path_mistral)

    else:
        response = connect_model.request_model(model, prompt)
        print(response)

        cleaned_dataset = data_set_creation.format_data(response)
        print(cleaned_dataset)

        data_set_creation.save_data(data_set_creation.format_data(response), file_path, save_path)


if __name__ == '__main__':
    main()
