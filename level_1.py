import pygame
from tile_creator import Tile_creator
from config import *

class Level_1:
  def __init__(self):
    self.screen = pygame.display.get_surface()
    self.background_group = pygame.sprite.Group()

    self.tile_creator = Tile_creator()

    self.create_map()

  def create_map(self):
    for row_index, row in enumerate(LEVEL_1_MAPa):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case " ":
            self.tile_creator.tile("grass", (x,y), [self.background_group])
          case "S":
            self.tile_creator.tile("sand", (x,y), [self.background_group])
          case "W":
            self.tile_creator.tile("water", (x,y), [self.background_group])

  def update(self):
    self.background_group.draw(self.screen)