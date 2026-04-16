import random

class MixWordService:
    @staticmethod
    def mix_word(word):
        max_nb_try = 10
        count_nb_try = 0
        result = word
        while result == word and count_nb_try < max_nb_try:
            if len(word) > 200:
                result =  ''
            else:
                result = ''.join(random.sample(word, k=len(word)))
            count_nb_try += 1
        return result