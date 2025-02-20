
from random import randint

SCREEN_SIZE = (400,300)
FPS = 60

TILE_SIZE = 32
#putting variables in all caps indicate variable shouldl nto be changed


ROW = 6      # Number of rows
COL = 12     # Number of columns

#random seed
for i in range(ROW):
  random = randint(0,3)
  if random == 0:
    row = [" "]
  if random >= 1:
    row = ["X"]
 # See note below
  LEVEL_1_MAP  = row * COL
  print(LEVEL_1_MAP, "\b,")     # Add a comma after each row

LEVEL_1_MAPa = [
[' ', 'X', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
]
#LEVEL_1_MAP  = (row, "\b,")


"""LEVEL_1_MAP = [
  ['X','X','X','X','X','X','X','X','X','X','X','X'],
  ['X',' ',' ',' ',' ','X',' ',' ',' ','X',' ','X'],
  ['X','X',' ','X','X','X',' ',' ','X','X',' ','X'],
  ['X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
  ['X','X','X','X','X','X','X','X','X','X','X','X']
]"""
#see matrix example code on how to generate many tiles at once