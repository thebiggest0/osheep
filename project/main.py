import connect_model
import data_set_creation
import process_text


def main():
    mistral = False
    model_mistral = "mistral"
    file_path_mistral = "../data/aida_dataset_mistral.json"
    save_path_mistral = "../data/aida_dataset_mistral.json"

    model_gemma = "gemma2"
    file_path_gemma = "../data/aida_dataset_gemma.json"
    save_path_gemma = "../data/aida_dataset_gemma.json"

    paragraphs = process_text.text_to_list()
    if mistral:
        for paragraph in paragraphs:
            print(paragraph)
            count = len(paragraph) // 100
            if count == 0:
                count = 1

            prompt_mistral = f'#based on the content, summarize the paragraph and return only a python list (nothing extra) which contains {count} different dictionaries of key ("instruction", "response") value pairs covering key points of the paragraph. Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "sentence explanation for the given prompt, per the instructions and context provided"}} ## content: "{paragraph}"'

            response = connect_model.request_model(model_mistral, prompt_mistral)
            print(1, response)

            ## TESTING ##
            # confirm response format is correct with AI
            data_set_creation.confirm_data_format(model_mistral, response)
            print(2, response)

            # use AI to provide input to each dictionary
            response = data_set_creation.create_input(model_mistral, response, paragraphs[0])
            print(3, response, "\n")

            data_set_creation.save_data(response, file_path_mistral, save_path_mistral)

    else:
        for paragraph in paragraphs:
            print(paragraph)
            count = len(paragraph) // 100
            if count == 0:
                count = 1

            model_mistral = "mistral"
            prompt_mistral = f'#based on the content, summarize the paragraph and return only a python list (nothing extra) which contains {count} different dictionaries each with keys ("instruction", "response") value pairs covering key points of the paragraph. Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "sentence explanation for the given prompt, per the instructions and context provided"}} ## content: "{paragraph}"'
            file_path_mistral = "../data/aida_dataset_mistral.json"
            save_path_mistral = "../data/aida_dataset_mistral.json"

            response = connect_model.request_model(model_gemma, prompt_mistral)
            print(1, response)

            ## TESTING ##
            # confirm response format is correct with AI
            data_set_creation.confirm_data_format(model_gemma, response)
            print(2, response)

            # use AI to provide input to each dictionary
            response = data_set_creation.create_input(model_gemma, response, paragraphs[0])
            print(3, response, "\n")

            data_set_creation.save_data(response, file_path_gemma, save_path_gemma)

    # model_mistral = "mistral"
    # prompt_mistral = f'#based on the content, summarize the paragraph and return only a python list (nothing extra) which contains 2 different dictionaries of key value pairs covering key points of the paragraph. Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "sentence explanation for the given prompt, per the instructions and context provided"}} ## content: "{paragraphs[0]}"'
    # file_path_mistral = "../data/aida_dataset_mistral.json"
    # save_path_mistral = "../data/aida_dataset_mistral.json"
    # mistral = True
    #
    # model = "gemma2"
    # prompt = f'#based on the ##content, summarize the paragraph and return only a python list (nothing extra) which contains 12 different dictionaries of key value pairs covering key points of the paragraph see ##Example for dictionary key value pair template. ##Example: {{"instruction": "natural language text input about a topic in this paragraph about AIDA", "response": "target output for the given prompt, per the instructions and context provided"}} ## content: "{paragraphs[0]}"'
    # file_path = "../data/dataset_aida_gemma.json"
    # save_path = "../data/dataset_aida_gemma.json"
    # # gemma = False
    #
    #
    # if mistral:
    #     response = connect_model.request_model(model_mistral, prompt_mistral)
    #     print(1, response)
    #
    #     ## TESTING ##
    #     # confirm response format is correct with AI
    #     # response = data_set_creation.confirm_data_format(model_mistral, response)
    #     data_set_creation.confirm_data_format(model_mistral, response)
    #     print(2, response)
    #
    #     # use AI to provide input to each dictionary
    #     response = data_set_creation.create_input(model_mistral, response, paragraphs[0])
    #     print(3, response)
    #
    #     data_set_creation.save_data(response, file_path_mistral, save_path_mistral)
    #
    #     ## OLD
    #     # cleaned_dataset = data_set_creation.format_data(response)
    #     # print(cleaned_dataset)
    #
    #     # data_set_creation.save_data(data_set_creation.format_data(response), file_path_mistral, save_path_mistral)
    #
    # else:
    #     response = connect_model.request_model(model, prompt)
    #     print(response)
    #
    #     cleaned_dataset = data_set_creation.format_data(response)
    #     print(cleaned_dataset)
    #
    #     data_set_creation.save_data(data_set_creation.format_data(response), file_path, save_path)


if __name__ == '__main__':
    main()
