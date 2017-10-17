import os

import markovify


def generate_markov_text(filename, file_format, number_lines):
    sentence_list = []
    dir = os.path.dirname(__file__)
    file_path = 'text_files/' + str(filename) + "." + str(file_format)
    filename = os.path.join(dir, file_path)
    with open(filename) as f:
        text = f.read()
    # Build model
    text_model = markovify.Text(text)
    for i in range(number_lines):
        sentence = text_model.make_sentence()
        sentence_list.append(sentence)
    return sentence_list


def generate_short_markov_text(filename, file_format, number_lines, size_of_sentence):
    sentence_list = []
    dir = os.path.dirname(__file__)
    file_path = 'text_files/' + str(filename) + "." + str(file_format)
    filename = os.path.join(dir, file_path)
    with open(filename) as f:
        text = f.read()
    # Build model
    text_model = markovify.Text(text)
    for i in range(number_lines):
        sentence = text_model.make_short_sentence(int(size_of_sentence))
        sentence_list.append(sentence)
    return sentence_list

