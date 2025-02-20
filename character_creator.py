import pygame
from character import Character

characters = {"basic": {"idle_right": "assets/character/idle/",
                        "walk_right": "assets/character/walk/",
                        "atk_right": "assets/character/atk/",
                        "jump":"assets/character/jump/",
                        "dies":"assets/character/dies/",},}

def char_basic(spawn_point, group):
  return Character(spawn_point, group, characters["basic"])
