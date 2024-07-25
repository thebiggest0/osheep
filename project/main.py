import connect_model
import data_set_creation
import process_text


def main():
    paragraphs = process_text.break_down_text()
    dataset = []
    for paragraph in paragraphs:
        count = paragraph[1] // 200

        model = "mistral"
        prompt = f'#based on the content, summarize the paragraph and return {count} dictionary of key value pairs. ' \
                 f'Example: {{"input": "topic of the paragraph", "response": "summary of the topic"}} ## content: {paragraph[0]}'

        response = connect_model.request_model(model, prompt)
        dataset.append(data_set_creation.format_data(response))

    data_set_creation.save_data(dataset)


if __name__ == '__main__':
    main()
