import pygame
import sys
from pygame.locals import QUIT


from utilities.config import *
from level_1 import Level_1

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('DESTROY DESTROY DESTROY DESTROY DESTROY DESTROY DESTROY DESTROY')
    
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    self.clock = pygame.time.Clock()
    #HAIYAYAIAYAYAYAIAIAYAAIYAIYIY
    self.level_1 = Level_1()

    while True:
      for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()

      self.level_1.update()
      
      pygame.display.update()
      self.clock.tick(FPS)