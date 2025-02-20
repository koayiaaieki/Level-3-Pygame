import pygame
import sys
from pygame.locals import QUIT


from config import *
#* means import everyything

from level_1 import Level_1

class Game:
  def __init__(self):
    pygame.init()

    pygame.display.set_caption('Tiles!')
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    self.clock = pygame.time.Clock()
    #gluck
    self.level_1 = Level_1()
    
  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

      self.level_1.update()

      pygame.display.update()

      self.clock.tick(FPS)
