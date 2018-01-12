from thesaurus import ThesaurusWord
from textstat.textstat import textstat
import time
from PyDictionary import PyDictionary
import csv


def create_index():
    with open('data_files/final_short.csv', 'r') as f:
        reader = csv.reader(f)

        return list(reader)


def create_index_list(object_list):

    index_list = []
    parsed_object_list = []

    for i in range(0, len(object_list)):
        if (object_list[i].tag == "ADJ") | (object_list[i].tag == "ADV") | \
                (object_list[i].tag == "VERB"):
            index_list.append(i)
            parsed_object_list.append(object_list[i])

    print("Create index list " + str())

    return index_list


def word_search(word, big):
    for i in range(0, len(big)):
        if str(word) == str(big[i][0]):

            if str(big[i][3]) is not None:
                return str(big[i][3]).partition(' ')[0]
            else:
                break
    return word


def word_replacer(index_list, original_list):

    BIG_LIST = create_index()


    dictionary = PyDictionary()

    for i in range(0, len(index_list)):

        current_word = original_list[index_list[i]].content

        print(current_word)

        try:
            #synonym = ThesaurusWord(current_word).synonyms(complexity=2)
            #synonym = dictionary.synonym(current_word)[0]

            synonym = word_search(current_word, BIG_LIST)

        except IndexError:
            synonym = current_word

        print(synonym)
        original_list[index_list[i]].content = synonym

    

    print("Word replacer " + str())

    return original_list
