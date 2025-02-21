import pygame
from utilities.config import *

class Camera_group(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.screen = pygame.display.get_surface()
    self.map_width_mid = SCREEN_SIZE[0] // 2
    self.map_height_mid = SCREEN_SIZE[1] // 2

  def draw(self, player):
    offset_x = player.rect.centerx - self.map_width_mid
    offset_y = player.rect.centery - self.map_height_mid
    for sprite in self.sprites():
      new_pos_x = sprite.rect.centerx - offset_x
      new_pos_y = sprite.rect.centery - offset_y
      self.screen.blit(sprite.image, (new_pos_x, new_pos_y))
      
  