class Word:

    def __init__(self, content, person, number, tense, tag):
        self.content = content
        self.person = person
        self.number = number
        self.tense = tense
        self.tag = tag


def create_word_list(json):

    word_list = []

    for i in range(0, len(json['tokens'])):
        word_list.append(Word(

            json['tokens'][i]['text']['content'],

            json['tokens'][i]['partOfSpeech']['person'],

            json['tokens'][i]['partOfSpeech']['number'],

            json['tokens'][i]['partOfSpeech']['tense'],

            json['tokens'][i]['partOfSpeech']['tag']

        ))

    return word_list


def create_raw_word_list(word_object_list):

    raw_words = []

    for i in range(0, len(word_object_list)):
        raw_words.append(word_object_list[i].content)

    return raw_words
