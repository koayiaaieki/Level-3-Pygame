import pygame
from tile_files.tile_creator import Tile_creator
from utilities.config import *
#char
from character_files.character_creator import Character_creator
#obs
from obstacle_files.obstacle_creator import Obstacles
#cam
from camera import Camera_group

class Level_1:
  def __init__(self):
    self.screen = pygame.display.get_surface()

    self.background_group = Camera_group()

    self.obstacle_group = Camera_group()
    self.obstacle_creator = Obstacles()

    self.tile_group = Camera_group()
    self.tile_creator = Tile_creator()

    self.player_group = Camera_group()
    self.character_creator = Character_creator()

    self.visible_group = Camera_group()

    self.create_map()

    self.create_obstacles()

    self.spawn_sprites()

#level uno map
  def create_map(self):
    for row_index, row in enumerate(LEVEL_1_MAPa):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case " ":
            self.tile_creator.tile("grass", (x,y), [self.background_group, self.visible_group])
          case "S":
            self.tile_creator.tile("sand", (x,y), [self.background_group, self.visible_group])
          case "W":
            self.tile_creator.tile("water", (x,y), [self.background_group, self.visible_group])
          case "L":
            self.tile_creator.tile("lilypad", (x,y), [self.background_group, self.visible_group])

#feet
  def create_obstacles(self):
    for row_index, row in enumerate(LEVEL_1_OBSTACLESa):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case "X":
            self.obstacle_creator.tile("bush", (x,y), [self.obstacle_group, self.visible_group])
          case "O":
            self.obstacle_creator.tile("rock", (x,y), [self.obstacle_group, self.visible_group])


  def spawn_sprites(self):
    for row_index, row in enumerate(LEVEL_1_SPRITES):
      for col_index, col in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        if col == "C":
          self.player = self.character_creator.char_basic((x,y), [self.player_group, self.visible_group], self.obstacle_group)

  def update(self):
    self.screen.fill('black')
    #map
    self.background_group.draw(self.player)
    #objacteesles
    self.obstacle_group.draw(self.player)
    self.visible_group.draw(self.player)
    #payer
    self.player_group.draw(self.player)
    self.player_group.update()