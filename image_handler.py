from os import walk
import pygame
from config import *

#ver 4.1
"""for path, folders, files in walk('assets/'):
    print(path)
    print(folders)
    print(files)

for path, folders, files in walk('pics/felix/'):
  for file_name in files:
    full_path = path + file_name
    print(full_path)"""

def import_folder(path):
    frame_list = []
    path_list = []

    for path, folders, files in walk(path):
      for file_name in files:
        full_path = path + file_name
        path_list.append(full_path)
    path_list.sort()

    for path in path_list:
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        frame_list.append(img)

    return frame_list