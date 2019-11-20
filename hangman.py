import time
class User_interface():
    failed_number = 0

    def __init__(self, word_given):
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
        print('Board:', end='')
        for letter in self.board:
            print('{} '.format(letter), end='')
        print()

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







