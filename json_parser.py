import time

class Word:

    def __init__(self, content, person, number, tense, tag):
        self.content = content
        self.person = person
        self.number = number
        self.tense = tense
        self.tag = tag


def create_word_list(json):

    start_time = time.time()

    word_list = []

    for i in range(0, len(json['tokens'])):
        word_list.append(Word(

            json['tokens'][i]['text']['content'],

            json['tokens'][i]['partOfSpeech']['person'],

            json['tokens'][i]['partOfSpeech']['number'],

            json['tokens'][i]['partOfSpeech']['tense'],

            json['tokens'][i]['partOfSpeech']['tag']

        ))

    end_time = time.time()

    print("Create word list " + str(end_time-start_time))

    return word_list


def create_raw_word_list(wordObjList):

    start = time.time()

    raw_words = []

    for i in range(0, len(wordObjList)):
        raw_words.append(wordObjList[i].content)

    end = time.time()

    print("Create raw word list " + str(end-start))

    return raw_words
