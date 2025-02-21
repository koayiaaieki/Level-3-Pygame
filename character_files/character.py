import pygame
from character_files.character_image import Image
from character_files.character_action import Action

class Character(pygame.sprite.Sprite):
  def __init__(self, position, groups, frames, obstacles):
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

    #collide and hanging myself
    self.obstacles = obstacles
    self.hitbox = self.rect.inflate(-36, -30) 

  def collide(self, direction):
    if direction == 'x':
      for obstacle in self.obstacles:
        if obstacle.rect.colliderect(self.hitbox):
          if self.direction_vector["x"] > 0:
            self.hitbox.right = obstacle.rect.left
          elif self.direction_vector["x"] < 0:
            self.hitbox.left = obstacle.rect.right
    if direction == 'y':
      for obstacle in self.obstacles:
        if obstacle.rect.colliderect(self.hitbox):
          if self.direction_vector["y"] > 0:
            self.hitbox.bottom = obstacle.rect.top
          elif self.direction_vector["y"] < 0:
            self.hitbox.top = obstacle.rect.bottom
    self.rect.center = self.hitbox.center

  # fxgfzdhhfdx
  def update(self):
    self.action_controller.update()
    self.image_controller.update()
      
  
    
    