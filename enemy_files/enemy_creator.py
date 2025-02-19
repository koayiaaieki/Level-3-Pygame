import pygame
from enemy_files.enemy import Enemy
from utilities.image_handler import *

class Enemy_creator():
  def __init__(self):
    self.enemy_file_path = {"fairy_liu": {"idle_right": "assets/enemy/fairyliu/fairyliu_idle/", 
                                          "huh": "assets/enemy/fairyliu/fairyliu_nnt/",},
                            "big_liu": {"idle_right": "assets/enemy/bigliu/", },
                            "special_liu": {"idle_right": "assets/enemy/specialliu/bigliu_eye/", 
                                             "mad": "assets/enemy/specialliu/bigliu_horn/",},}
    
    self.enemy_frames = {}
    self.populate_right_frames()
    self.populate_left_frames()

  def populate_right_frames(self):
    for key in self.enemy_file_path:
      list = get_all_frames(self.enemy_file_path[key])
      self.enemy_frames.update({key: list})

  def populate_left_frames(self):
    for enemy in self.enemy_frames:
      list = flip_frames(self.enemy_frames[enemy]["idle_right"])
      self.enemy_frames[enemy].update({"idle_left": list})
      
  def enemy(self, type, spawn_point, group):
    return Enemy(spawn_point, group, self.enemy_frames[type])