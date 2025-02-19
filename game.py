import pygame
import sys
from pygame.locals import QUIT


from utilities.config import *
from level_1 import Level_1
from level_2 import Level_2

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('The Legend Of Asthma: Alvin')
    
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    self.clock = pygame.time.Clock()
    
    self.level_1 = Level_1()
    self.level_2 = Level_2()

    self.what = pygame.image.load("assets/fx/non.png").convert_alpha()
    self.what = pygame.transform.scale(self.what, (800,600))

    self.game_state()
    
  def game_state(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        self.level_2.update()

    while True:
      for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()

      self.level_1.update()

      self.screen.blit(self.what, (0,0))
      
      pygame.display.update()
      self.clock.tick(FPS)