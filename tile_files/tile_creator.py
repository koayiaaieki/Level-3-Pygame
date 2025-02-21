import pygame
from tile_files.tile import Tile

class Tile_creator():
  def __init__(self):
    self.tile_file_path = {"grass": "assets/environment/grass.jpeg",
                           "sand":  "assets/environment/sand.png",
                           "water":  "assets/environment/water.png",
                           "lilypad":  "assets/environment/lilypad.jpg",}
    
    self.tile_images = {}

    self.populate_image()

  def populate_image(self):
    for key in self.tile_file_path:
      img = pygame.image.load(self.tile_file_path[key]).convert_alpha()
      self.tile_images.update({key: img})

  def tile(self, type, position, groups):
    return Tile(self.tile_images[type], position, groups)