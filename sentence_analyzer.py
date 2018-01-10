from thesaurus import ThesaurusWord
from textstat.textstat import textstat
import time
from PyDictionary import PyDictionary


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


def word_replacer(index_list, original_list):

    dictionary = PyDictionary()

    for i in range(0, len(index_list)):

        current_word = original_list[index_list[i]].content

        try:
            #synonym = ThesaurusWord(current_word).synonyms(complexity=2)
            synonym = dictionary.synonym(current_word)[0]

        except IndexError:
            synonym = current_word

        original_list[index_list[i]].content = synonym

    

    print("Word replacer " + str())

    return original_list
