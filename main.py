import User_interface
import word

words_list = ['altitude', 'attitude', 'curtain', 'cat']


class Hangman:
    def __init__(self, word_received):
        self.word = word.Word_hangman(word_received)
        self.interface = User_interface.User_interface(word_received)

    def start_game(self):
        while not self.interface.complete_or_not:
            guessed_letter = self.interface.update_input()
            self.interface.update_interface(self.word.update_word(guessed_letter))


for word_given in words_list:
    hangman_game = Hangman(word_given)
    hangman_game.start_game()
