import random
import csv


class SentenceGenerator:
    """Takes 'words.csv' file saved in the project folder and generates a random
    sentence. First letter is capitalised and a full stop is added at the end. The
    csv file is converted into a dictionary once when calling the class"""

    def __init__(self):
        # Maximum character length of the sentence.
        self.target_length = 70
        # csv file containing two columns, sequential number and word, no titles.
        self.words_source = "words.csv"
        self.words_dict = {}

        # Load words from csv file into dictionary only once when class is called.
        if self.words_dict == {}:
            self.build_dictionary(self.words_source)

    def build_dictionary(self, source):
        """Takes local file titled 'words.csv' and populates dictionary with
        its contents."""
        with open(source, mode="r") as file:
            reader = csv.reader(file)
            self.words_dict = {row[0]: row[1] for row in reader}

    def build_random_sentence(self):
        """Returns a random sentence by picking random words from the words_dict
        to a maximum character length defined by target_length"""
        dict_len = len(self.words_dict)
        sentence = ""
        while len(sentence) < self.target_length:
            # Pick random number between 1 and length of dictionary of words.
            random_key = str(random.randint(1, dict_len))
            random_word = self.words_dict[random_key]

            # Make first letter title case.
            if sentence == "":
                sentence += random_word.title()
            else:
                sentence += " " + random_word
        sentence += "."
        return sentence
