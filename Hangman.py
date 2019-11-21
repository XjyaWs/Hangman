import pyxel
import string


class Hangman_game:

    def __init__(self, words_list):
        pyxel.init(180, 80)
        pyxel.load('hangman.pyxres')
        self.words_list = words_list
        self.words_count = 0

        self.head = (0, 0)
        self.body1 = (16, 0)
        self.body2 = (32, 0)
        self.body3 = (0, 16)
        self.leg1 = (48, 0)
        self.leg2 = (16, 16)
        self.blank = (160, 160)
        self.updated_word = list(self.words_list[self.words_count])

        # screen update data
        self.board = list('_' * len(self.words_list[self.words_count]))
        self.board_text = ''.join(self.board)
        self.show_input = True
        self.show_answer = False
        self.show_result = False
        self.update_board = True
        self.completed = False
        self.failed = False
        self.answer = ''
        self.failed_number = 0
        self.win = False
        self.lose = False

        pyxel.run(self.update, self.draw)

    def data_init(self, word_given):
        self.updated_word = list(word_given)

        # screen update data
        self.board = list('_' * len(word_given))
        self.board_text = ''.join(self.board)
        self.show_input = True
        self.show_answer = False
        self.show_result = False
        self.update_board = True
        self.completed = False
        self.failed = False
        self.answer = ''
        self.failed_number = 0
        self.win = False
        self.lose = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_ENTER):
            if self.completed:
                self.words_count += 1
                if self.words_count >= len(self.words_list):
                    pyxel.quit()
                self.data_init(self.words_list[self.words_count])
            else:
                # update result
                if pyxel.btnp(pyxel.KEY_ENTER) and not self.completed:
                    self.show_result = True
                    self.update_board = True
                    if self.failed:
                        self.failed_number += 1

        # update answer
        for index, letter in enumerate(string.ascii_lowercase):
            if pyxel.btnp(index + 18):
                self.show_result = False
                self.answer = letter
                self.update_word(letter)
                self.show_answer = True
                self.update_board = False

        if '_' not in self.board_text:
            self.win = True
            self.completed = True

        if self.failed_number == 6:
            self.lose = True
            self.completed = True

    def update_word(self, guessed_letter):
        if guessed_letter in self.updated_word:
            for index, letter in enumerate(self.updated_word):
                if letter == guessed_letter:
                    self.updated_word[index] = '$'
                    self.board[index] = letter
            self.failed = False
        else:
            self.failed = True

    def draw(self):
        # fix background
        pyxel.cls(0)

        # Hangman update
        if self.failed_number == 0:
            self.draw_hangman(self.head, self.body1, self.leg1)
        elif self.failed_number == 1:
            self.draw_hangman(self.head, self.body1, self.leg2)
        elif self.failed_number == 2:
            self.draw_hangman(self.head, self.body1, self.blank)
        elif self.failed_number == 3:
            self.draw_hangman(self.head, self.body2, self.blank)
        elif self.failed_number == 4:
            self.draw_hangman(self.head, self.body3, self.blank)
        elif self.failed_number == 5:
            self.draw_hangman(self.head, self.blank, self.blank)
        elif self.failed_number == 6:
            self.draw_hangman(self.blank, self.blank, self.blank)

        # Board update
        if self.update_board:
            self.board_text = ''.join(self.board)
        pyxel.text(15, 10, self.board_text, 7)

        # Input update
        if self.show_input:
            pyxel.text(60, 20, 'Please guess a letter:', 7)

        # answer update
        if self.show_answer:
            pyxel.text(60, 40, self.answer, 7)

        # result update
        if self.show_result:
            if self.failed:
                pyxel.text(60, 60, 'Wrong!', 7)
            else:
                pyxel.text(60, 60, 'Correct!', 7)

        if self.win:
            pyxel.text(110, 60, 'You win!', 11)
        if self.lose:
            pyxel.text(110, 60, 'You Lose!', 8)

    def draw_hangman(self, head_set, body_set, leg_set):
        pyxel.blt(15, 25, 0, head_set[0], head_set[1], 16, 16)
        pyxel.blt(15, 25 + 16, 0, body_set[0], body_set[1], 16, 16)
        pyxel.blt(15, 25 + 32, 0, leg_set[0], leg_set[1], 16, 16)

