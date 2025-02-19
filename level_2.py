import pygame
from tile_files.tile_creator import Tile_creator
from utilities.config import *
#char
from character_files.character_creator import Character_creator
#obs
from obstacle_files.obstacle_creator import Obstacles
#cam
from camera import Camera_group

class Level_2:
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
    pygame.mixer.music.load('assets/audio/yeaha.wav')

    #what
    self.gfx = pygame.image.load('assets/fx/vignette.png').convert_alpha()
    self.gfx = pygame.transform.scale(self.gfx, (800,600))

    self.create_map()

    #self.create_obstacles()

    #self.spawn_sprites()

    pygame.mixer.music.play()

  def create_map(self):
    for row_index, row in enumerate(LEVEL_2_MAP):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case "X":
            self.obstacle_creator.tile("rock", (x,y), [self.obstacle_group, self.visible_group])
          case "C":
            self.player = self.character_creator.char_basic((x,y), [self.player_group, self.visible_group], self.obstacle_group)

  def update(self):
    self.screen.fill((128,128,128))
    self.screen.blit(self.gfx, (0,0))
    self.visible_group.draw(self.player)
    self.player_group.update()

"""this level is unfinished, if you want to try this level out, go to game.py and chage
self.level_1.update() to self.level_2.update() in the While loop

    while True:
      for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()

      self.level_1.update()
      ^^^^^^this one 

      self.screen.blit(self.what, (0,0))
      
      pygame.display.update()
      self.clock.tick(FPS)
      
      """