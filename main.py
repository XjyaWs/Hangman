import hangman
import random

words_list = ['petrol', 'northeastern', 'west', 'north', 'south', 'vocabulary', 'gossip', 'series', 'altitude', 'glacier', 'waterfall', 'rapids', 'meander', 'delta']
random.shuffle(words_list)
hangman.HangmanGame(words_list)
