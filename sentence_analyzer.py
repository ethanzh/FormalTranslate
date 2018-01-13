from PyDictionary import PyDictionary
import csv


def create_index():  # Creates a Python list from a CSV thesaurus file
    with open('data_files/final_short.csv', 'r') as f:
        reader = csv.reader(f)

        return list(reader)


def create_index_list(object_list):  # Creates a list of indexes of words to be replaced, based on their tag

    index_list = []
    parsed_object_list = []

    for i in range(0, len(object_list)):
        if (object_list[i].tag == "ADJ") | (object_list[i].tag == "ADV") | \
                (object_list[i].tag == "VERB"):
            index_list.append(i)
            parsed_object_list.append(object_list[i])

    print("Create index list " + str())

    return index_list


def word_search(word, big):  # Searches the CSV to see if there is a match. Returns first synonym
    for i in range(0, len(big)):

        if (str(word) == str(big[i][0])) & (str(big[i][3]) is not None):

            return str(big[i][3]).partition(' ')[0]

    return word


def word_replacer(index_list, original_list):

    parsed_list = original_list

    thesaurus_csv = create_index()

    for i in range(0, len(index_list)):

        current_word = parsed_list[index_list[i]].content

        try:
            # synonym = ThesaurusWord(current_word).synonyms(complexity=2)  # Uses Thesaurus API instead of my list

            synonym = word_search(current_word, thesaurus_csv)

        except IndexError:
            synonym = current_word  # When using ThesaurusWord, if complexity isn't there, return original word

        parsed_list[index_list[i]].content = synonym

    return parsed_list
