import pygame
from utilities.config import *

class feet(pygame.sprite.Sprite):
  def __init__(self, image, position, groups):
    super().__init__(groups)

    self.image = image

    self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    self.rect = self.image.get_rect(topleft=position)

#change obstacle_grup to rock_group and bush_group later