
from random import randint

SCREEN_SIZE = (800,600)
FPS = 60

TILE_SIZE = 64
#putting variables in all caps indicate variable shouldl nto be changed


LEVEL_1_MAPa = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
['S', 'S', 'S', ' ', 'S', ' ', 'S', ' ', 'S', 'S', 'S', ' ',' '],
['S', ' ', ' ', ' ', 'S', ' ', 'S', ' ', 'S', ' ', ' ', ' ',' '],
['S', 'S', 'S', ' ', 'S', ' ', 'S', ' ', 'S', 'S', 'S', ' ',' '],
[' ', ' ', 'S', ' ', 'S', ' ', 'S', ' ', ' ', ' ', 'S', ' ',' '],
['S', 'S', 'S', ' ', 'S', 'S', 'S', ' ', 'S', 'S', 'S', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
]
#LEVEL_1_MAP  = (row, "\b,")
#see matrix example code on how to generate many tiles at once

LEVEL_1_OBSTACLES = [
['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
['O', 'O', 'O', ' ', 'O', ' ', 'O', 'X', 'O', 'O', 'O', ' ',' '],
[' ', ' ', ' ', 'X', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
['O', ' ', 'O', 'X', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ','X'],
[' ', ' ', 'O', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'O', ' ',' '],
['O', 'O', 'O', ' ', 'O', 'O', 'O', ' ', 'O', 'O', 'O', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
]
#LEVEL_1_MAP  = (row, "\b,")
#see matrix example code on how to generate many tiles at once