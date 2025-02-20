import pygame
from config import *

class Tile(pygame.sprite.Sprite):
  def __init__(self, position, groups):
    super().__init__(groups)

    self.image = pygame.image.load('assets/environment/grass.jpeg').convert_alpha()

    self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    self.rect = self.image.get_rect(topleft=position)
