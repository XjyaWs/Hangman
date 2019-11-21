import time
import pyxel
import string

class User_interface():

    def __init__(self, word_given):
        pyxel.init(180, 80)
        pyxel.load('hangman.pyxres')
        self.head = (0, 0)
        self.body1 = (16, 0)
        self.body2 = (32, 0)
        self.body3 = (0 , 16)
        self.leg1 = (48, 0)
        self.leg2 = (16, 16)
        self.updated_word = list(word_given)
        self.board = list('_'*len(word_given))
        self.complete_or_not = False
        self.failed = False
        self.failed_number = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            pyxel.quit()
        for index, letter in enumerate(string.ascii_lowercase):
            if pyxel.btnp(index + 18):
                pyxel.text(60, 40, letter, 7)
                self.update_word(letter)
        if pyxel.btnp(pyxel.KEY_ENTER):
            if not self.failed:
                pyxel.text(60, 60, 'Correct!', 7)
            else:
                pyxel.text(60, 60, 'Wrong!', 7)

    def update_word(self, guessed_letter):
        if guessed_letter in self.updated_word:
            for index, letter in enumerate(self.updated_word):
                if letter == guessed_letter:
                    self.updated_word[index] = '$'
                    self.board[index] = letter
            self.failed = False
            self.failed_number += 1
        else:
            self.failed = True

    def draw(self):
        
        # Hangman update
        pyxel.blt(15, 25, 0, self.head[0], self.head[1], 16, 16)
        pyxel.blt(15, 25 + 16, 0, self.body1[0], self.body1[1], 16, 16)
        pyxel.blt(15, 25 + 32, 0, self.leg1[0], self.leg1[1], 16, 16)

        # Board update
        text = ''.join(self.board)
        pyxel.text(15, 10, text, 7)

        # Input update
        pyxel.text(60, 20, 'Please guess a letter:', 7)

        # answer update

        
        #result update


    def update_interface(self, data):
        print('--------------------------------')

        # receive data
        index_list = data[0]
        failed_or_not = data[1]
        guessed_letter = data[2]

        # update guess result
        if failed_or_not == True:
            time.sleep(1)
            print('Not correct!')
            self.stages.pop(1)
            self.failed_number = self.failed_number + 1
        else:
            time.sleep(1)
            print('Correct!')

        # update board
        for index in index_list:
            self.board[index] = guessed_letter
        time.sleep(1)
        print('Board:', end='')
        for letter in self.board:
            print('{} '.format(letter), end= '')
        print()

        # update hangman result
        for row in self.stages:
            print(row)
        print('--------------------------------')
        if self.failed_number >= 6:
            print('You Failed!')
            self.complete_or_not = True
        if '_' not in self.board:
            print('Success!')
            self.complete_or_not = True

User_interface('wangshuang')





