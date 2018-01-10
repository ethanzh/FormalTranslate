from thesaurus import ThesaurusWord
from textstat.textstat import textstat



def create_index_list(object_list):
    index_list = []
    parsed_object_list = []

    for i in range(0, len(object_list)):
        if (object_list[i].tag == "ADJ") | (object_list[i].tag == "ADV") | \
                (object_list[i].tag == "VERB"):
            index_list.append(i)
            parsed_object_list.append(object_list[i])

    return index_list


def word_replacer(index_list, original_list):

        for i in range(0, len(index_list)):

            current_word = original_list[index_list[i]].content

            synonym = ThesaurusWord(current_word).synonyms(complexity=2)[0]

            original_list[index_list[i]].content = synonym

        return original_list
