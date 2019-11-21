import time
import pyxel

class User_interface():
    failed_number = 0

    def __init__(self, word_given):
        pyxel.init(100, 80)
        pyxel.load('hangman.pyxres')
        self.head = (0, 0)
        self.body1 = (16, 0)
        self.body2 = (32, 0)
        self.body3 = (0 , 16)
        self.leg1 = (48, 0)
        self.leg2 = (16, 16)
        self.stages = ["",
                       " ",
                       "| ",
                       "|----| ",
                       "|    0 ",
                       "|   /|\ ",
                       "|   / \ ",
                       "| "
                       ]

        self.board = list('_'*len(word_given))
        self.complete_or_not = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.blt(15, 25, 0, self.head[0], self.head[1], 16, 16)
        pyxel.blt(15, 25 + 16, 0, self.body1[0], self.body1[1], 16, 16)
        pyxel.blt(15, 25 + 32, 0, self.leg1[0], self.leg1[1], 16, 16)
        text = ''.join(self.board)
        pyxel.text(15, 10, text, 7)
        pyxel.show()

    def update_input(self):
        guessed_letter = input('Please guess a letter: \n')
        return guessed_letter


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





