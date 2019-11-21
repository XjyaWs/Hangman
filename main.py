import Hangman
import random

words_list = ['petrol', 'northeastern', 'west', 'north', 'south', 'vocabulary', 'gossip', 'series', 'altitude', 'glacier', 'waterfall', 'rapids', 'meander', 'delta']
random.shuffle(words_list)
Hangman.Hangman_game(words_list)
