import pygame

class Action:
  def __init__(self, player):
      self.player = player

  def decide_action(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
       action = "atk"
       
    if self.player.direction_vector['x'] != 0 or self.player.direction_vector['y'] != 0:
        action = "walk"
    else:
        action = "idle"

    self.player.action = action

  def decide_direction(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        self.player.direction_vector['y'] = -1
        self.player.direction = "right"
    elif keys[pygame.K_DOWN]:
        self.player.direction_vector['y'] = 1
        self.player.direction = "right"
    else:
        self.player.direction_vector['y'] = 0

    if keys[pygame.K_RIGHT]:
        self.player.direction_vector['x'] = 1
        self.player.direction = "right"
    elif keys[pygame.K_LEFT]:
        self.player.direction_vector['x'] = -1
        self.player.direction = "left"
    else:
        self.player.direction_vector['x'] = 0

  def decide_current_action(self):
    self.decide_action()
    self.decide_direction()
    self.player.current_action = f"{self.player.action}_{self.player.direction}"
    
  def move(self):
    self.player.rect.centerx += self.player.direction_vector['x']*self.player.speed
    self.player.hitbox.centerx = self.player.rect.centerx
    self.player.collide("x")
    self.player.rect.centery += self.player.direction_vector['y']*self.player.speed
    self.player.hitbox.centery = self.player.rect.centery
    self.player.collide("y")

  def update(self):
    self.decide_current_action()
    self.move()