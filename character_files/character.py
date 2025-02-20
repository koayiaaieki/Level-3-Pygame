import pygame
from character_files.character_image import Image
from character_files.character_action import Action

class Character(pygame.sprite.Sprite):
  def __init__(self, position, groups, frames):
    super().__init__(groups)
    
    # frem
    self.frames = frames
    self.frame_index = 0
    self.frame_speed = 0.2
    
    # moveee
    self.direction_vector = {'x':0, 'y':0}
    self.speed = 5

    # wompow!
    self.action = "idle"
    self.direction = "right"
    self.current_action = f"{self.action}_{self.direction}"

    # erect
    self.image = self.frames["idle_right"][0]
    self.rect = self.image.get_rect(topleft = position)

    # CONTROOOOOOOOOOOOOOOOOOL
    self.image_controller = Image(self)
    self.action_controller = Action(self)

  # Update is updated to make all required method calls
  def update(self):
    self.action_controller.update()
    self.image_controller.update()
      
    
    