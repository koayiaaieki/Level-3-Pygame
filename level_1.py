import pygame
from tile_files.tile_creator import Tile_creator
from utilities.config import *
#char
from character_files.character_creator import Character_creator
from enemy_files.enemy_creator import Enemy_creator
#obs
from obstacle_files.obstacle_creator import Obstacles
#cam
from camera import Camera_group

pygame.init()
pygame.mixer.init()

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

    self.enemy_group = Camera_group()
    self.enemy_creator = Enemy_creator()


    self.visible_group = Camera_group()
    pygame.mixer.music.load('assets/audio/yeaha.wav')

    self.create_map()

    self.spawn_sprites()

    self.create_obstacles()

    self.create_decor()

    self.spawn_enemies()

    pygame.mixer.music.play()

#level uno map
  def create_map(self):
    for row_index, row in enumerate(LEVEL_1_MAP):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        #floor
        match tile:
          case " ":
            self.tile_creator.tile("grass", (x,y), [self.background_group, self.visible_group])
          case "S":
            self.tile_creator.tile("sand", (x,y), [self.background_group, self.visible_group])
          case "L":
            self.tile_creator.tile("lilypad", (x,y), [self.background_group, self.visible_group])

  def create_decor(self):
      for row_index, row in enumerate(LEVEL_1_DECOR):
        for col_index, tile in enumerate(row):
          x = col_index * TILE_SIZE
          y = row_index * TILE_SIZE
          #obstacles
          match tile:
            case "X":
              self.tile_creator.tile("bush", (x,y), [self.background_group, self.visible_group])

  def create_obstacles(self):
      for row_index, row in enumerate(LEVEL_1_OBS):
        for col_index, tile in enumerate(row):
          x = col_index * TILE_SIZE
          y = row_index * TILE_SIZE
          #obstacles
          match tile:
            case "W":
              self.obstacle_creator.tile("water", (x,y), [self.obstacle_group, self.visible_group])
            case "O":
              self.obstacle_creator.tile("rock", (x,y), [self.obstacle_group, self.visible_group])

  def spawn_sprites(self):
      for row_index, row in enumerate(LEVEL_1_SPRITES):
        for col_index, col in enumerate(row):
          x = col_index * TILE_SIZE
          y = row_index * TILE_SIZE
          if col == "C":
            self.player = self.character_creator.char_basic((x,y), [self.player_group, self.visible_group], self.obstacle_group)

  def spawn_enemies(self):
      for row_index, row in enumerate(LEVEL_1_SPRITES2):
        for col_index, col in enumerate(row):
          x = col_index * TILE_SIZE
          y = row_index * TILE_SIZE
          if col == "F":
            self.enemy_creator.enemy("fairy_liu", (x,y), [self.enemy_group, self.visible_group])
          if col == "M":
            self.enemy_creator.enemy("big_liu", (x,y), [self.enemy_group, self.visible_group])
          if col == "E":
            self.enemy_creator.enemy("special_liu", (x,y), [self.enemy_group, self.visible_group])

  def update(self):
    self.screen.fill('black')
    #map
    self.background_group.draw(self.player)

    #objacteesles
    self.enemy_group.draw(self.player)
    self.enemy_group.update()
    self.obstacle_group.draw(self.player)
    self.visible_group.draw(self.player)

    #payer
    self.player_group.draw(self.player)
    self.player_group.update()
