# Process text to analyze and train model


def break_down_text():
    '''
    break down the text to paragraphs and store each paragraph and their length in a list
    '''
    file_path = "../data/text_to_summarize.txt"
    with open(file_path, "r") as text:
        new_text = text.read()

    list_paragraphs = [new_text, len(new_text)]

    return list_paragraphs


def text_to_list():
    file_path = "../data/text_to_summarize.txt"
    with open(file_path, "r") as text:
        new_text = text.read()

    list_paragraphs = new_text.split("***")
    list_paragraphs = [paragraph.strip() for paragraph in list_paragraphs]
    return list_paragraphs
