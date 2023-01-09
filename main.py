from ui import TypingSpeed
from sentence_generator import SentenceGenerator

# ##################################################################################################### #
# The sentences used in this test are randomly generated from a list stored in the 'words.csv' file.    #
# The list consists of the 100 most common words as well as the 100 most common nouns.                  #
# 100 most common words, source Wikipedia:                                                              #
# https://en.wikipedia.org/wiki/Most_common_words_in_English                                            #
# 100 most common nouns, source espressoenglish:                                                        #
# https://www.espressoenglish.net/100-common-nouns-in-english/                                          #
# ##################################################################################################### #

# Create object from SentenceGenerator class.
generator = SentenceGenerator()
# Create gui object from TypingSpeed class with SentenceGenerator object.
app = TypingSpeed(generator)
