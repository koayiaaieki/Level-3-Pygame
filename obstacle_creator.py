import pygame
from obstacle import feet

class Obstacles():
  def __init__(self):
    self.tile_file_path = {"bush": "assets/obstacles/bush.png",
                           "rock":  "assets/obstacles/rock.png",}

    self.tile_images = {}

    self.populate_image()

  def populate_image(self):
    for key in self.tile_file_path:
      img = pygame.image.load(self.tile_file_path[key]).convert_alpha()
      self.tile_images.update({key: img})

  def tile(self, type, position, groups):
    return feet(self.tile_images[type], position, groups)
  
