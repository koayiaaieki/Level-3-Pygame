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
#ver 5.2
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

def get_all_frames(dictionary):
   new_dict = {}

   for key in dictionary:
      frame_list = import_folder(dictionary[key])
      new_dict.update({key: frame_list})

   return new_dict
#ver 6.0
def flip_frames(frame_list):
    new_list = []

    for frame in frame_list:
            flipped_frame = pygame.transform.flip(frame, True, False)
            flipped_frame.set_colorkey((0, 0, 0))
            new_list.append(flipped_frame)

    return new_list
