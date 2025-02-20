from character_files.character import Character
from utilities.image_handler import get_all_frames, flip_frames

class Character_creator():
  def __init__(self):
    self.characters = {"basic": {"idle_right": "assets/character/idle/",
                        "walk_right": "assets/character/walk/",
                        "atk_right": "assets/character/atk/",
                        "jump":"assets/character/jump/",
                        "dies":"assets/character/dies/",},}

    self.animation_frames = get_all_frames(self.characters["basic"])
    self.animation_frames.update({"idle_left":flip_frames(self.animation_frames["idle_right"])})
    self.animation_frames.update({"walk_left":flip_frames(self.animation_frames["walk_right"])})

  def char_basic(self, position, group):
    return Character(position, group, self.animation_frames)