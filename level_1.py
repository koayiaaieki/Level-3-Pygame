import pygame
from tile_creator import Tile_creator
from obstacle_creator import Obstacles
from character import Character
from config import *

class Level_1:
  def __init__(self):
    self.screen = pygame.display.get_surface()
    self.background_group = pygame.sprite.Group()
    self.obstacle_group = pygame.sprite.Group()

    self.visible_group = pygame.sprite.Group()
    self.player_group = pygame.sprite.Group()

    self.tile_creator = Tile_creator()
    self.obstacle_creator = Obstacles()

    self.create_map()

    self.create_obstacles()

    self.spawn_sprites()

#level uno map
  def create_map(self):
    for row_index, row in enumerate(LEVEL_1_MAP):
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

#feet
  def create_obstacles(self):
    for row_index, row in enumerate(LEVEL_1_OBSTACLES):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case "X":
            self.obstacle_creator.tile("bush", (x,y), [self.obstacle_group])
          case "O":
            self.obstacle_creator.tile("rock", (x,y), [self.obstacle_group])

  def spawn_sprites(self):
    for row_index, row in enumerate(LEVEL_1_SPRITES):
      for col_index, col in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        if col == "C":
          self.player = Character((x,y), [self.player_group])

  def update(self):
    #map
    self.background_group.draw(self.screen)
    #objacteesles
    self.obstacle_group.draw(self.screen)
    self.visible_group.draw(self.screen)
    #ppayer
    self.player_group.draw(self.screen)
    self.player_group.update()