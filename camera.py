import pygame
from utilities.config import *

class Camera_group(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.screen = pygame.display.get_surface()
    self.map_width_mid = SCREEN_SIZE[0] // 2
    self.map_height_mid = SCREEN_SIZE[1] // 2

  def draw(self, player):
    offset_x = max(0, player.rect.x - self.map_width_mid)
    if player.rect.x > 800:
      offset_x = min(1700, player.rect.x - self.map_width_mid)
    # ex) 700 - 400 = 300 right (-300)
    offset_y = max(0, player.rect.y - self.map_height_mid)
    if player.rect.y > 600:
      offset_y = min(1200, player.rect.y - self.map_height_mid)
    # ex) 550 - 300 = 250 down (-250)

    for sprite in self.sprites():
      new_pos_x = sprite.rect.centerx - offset_x #= positive
      new_pos_y = sprite.rect.centery - offset_y #= positive
      self.screen.blit(sprite.image, (new_pos_x, new_pos_y))
      