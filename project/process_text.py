# Process text to analyze and train model


def break_down_text():
    '''
    break down the text to paragraphs and store each paragraph and their length in a list
    '''
    file_path = "../data/text_to_summarize.txt"
    with open(file_path, "r") as text:
        new_text = text.read()

    paragraphs = new_text.split("\n")
    list_paragraphs = []
    for i in range(len(paragraphs)):
        n = len(paragraphs)
        list_paragraphs.append([paragraphs[i], n])

    return list_paragraphs
