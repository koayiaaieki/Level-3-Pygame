import pygame
from tile import Tile
from config import *

class Level_1:
  def __init__(self):
    self.screen = pygame.display.get_surface()

    self.tile_group = pygame.sprite.Group()

    self.create_map()

  def create_map(self):
    for row_index, row in enumerate(LEVEL_1_MAPa):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE

        if tile == "X":
          Tile((x, y), [self.tile_group])

  def update(self):
    self.tile_group.draw(self.screen)
