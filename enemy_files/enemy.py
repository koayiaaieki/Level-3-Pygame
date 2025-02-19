import pygame
from random import randint, choice

class Enemy(pygame.sprite.Sprite):
  def __init__(self, position, groups, frames):
    super().__init__(groups)

    #Frames
    self.animation_frames = frames
    
    # Image and Rect
    self.image = self.animation_frames["idle_right"][0]
    self.rect = self.image.get_rect(topleft = position)

    # Frame Control
    self.frame_index = randint(0, 10)/10
    self.frame_speed = randint(3, 10)/100
    
    # Character Control
    self.action = "idle_right"

    # Enemy Hitbox
    self.hitbox = self.rect.inflate(50, 50)

    ###### Patrol ######
    # set the next time to move randomly between 3 and 5 seconds (multipled by 1000 as time is calculated in milliseconds)
    self.next_move = pygame.time.get_ticks() + randint(7,10)*1000
    # Keep track of whether the sprite is already moving
    self.moving = False
    # choice(list) allows a random selection of an element from the list
    self.direction = choice([1, -1])

  # Check to see if sprite should move
  def check_move(self):
    if self.moving:
      self.move()
    else:
      self.check_time()
      
  def check_time(self):
    if pygame.time.get_ticks() >= self.next_move:
      self.random_movement_stats()
      self.moving = True
      
  # randomly re-rolls moving parameters (speed, direction, time)
  def random_movement_stats(self):
    self.direction = choice([1, -1])
    # Control move speed
    self.movespeed = randint(1,4) * self.direction
    self.next_move = pygame.time.get_ticks() + randint(7,10)*1000
    self.target_x = self.rect.x + (randint(30,70) * self.direction)

  def move(self):
    if self.moving:
      self.rect.centerx += self.movespeed
      if self.direction == 1 and self.rect.centerx >= self.target_x:
        self.moving = False
      elif self.direction == -1 and self.rect.centerx <= self.target_x:
        self.moving = False

  def check_status(self):
    if self.moving:
      if self.direction == 1:
        self.action = "idle_right"
      else:
        self.action = "idle_left"

  
  def animate(self):
    self.frame_index += self.frame_speed
    if self.frame_index >= len(self.animation_frames[self.action]):
      self.frame_index = 0
    self.image = self.animation_frames[self.action][int(self.frame_index)]

  def update(self):
    self.check_move()
    self.check_status()
    self.animate()