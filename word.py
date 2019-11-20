class Word_hangman():
    updated_word = []
    def __init__(self, word):
        self.updated_word = list(word)

    def update_word(self, guessed_letter):
        '''
        :param guessed_letter:
        :return: (index_list, failed_or_not, guessed_letter)
        '''
        index_list = []
        failed_or_not = True
        if guessed_letter in self.updated_word:
            for index, letter in enumerate(self.updated_word):
                if letter == guessed_letter:
                    self.updated_word[index] = '$'
                    index_list.append(index)
            failed_or_not = False
        return index_list, failed_or_not, guessed_letter