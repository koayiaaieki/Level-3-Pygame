import pygame
from config import *
from image_handler import *

class Character(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.animation_frame = import_folder('assets/character/idle/')
        self.image = self.animation_frame[0]
        self.rect = self.image.get_rect(topleft=position)
        self.frame_index = 0

        #move
        self.direction = {'x': 0, 'y': 0}
        self.speed = 5

        # fraem
        self.frame_rate = 0.05

    def input(self):
        keys = pygame.key.get_pressed()
        #y 
        if keys[pygame.K_UP]:
            self.direction['y'] = -1
        elif keys[pygame.K_DOWN]:
            self.direction['y'] = 1
        else:
            self.direction['y'] = 0
        #x 
        if keys[pygame.K_RIGHT]:
            self.direction['x'] = 1
        elif keys[pygame.K_LEFT]:
            self.direction['x'] = -1
        else:
            self.direction['x'] = 0

    def move(self):
        self.rect.centerx += self.direction['x'] * self.speed
        self.rect.centery += self.direction['y'] * self.speed

    def animate(self):
        self.frame_index += self.frame_rate
        if self.frame_index >= len(self.animation_frame):
            self.frame_index = 0
        self.image = self.animation_frame[int(self.frame_index)]

    def update(self):
        self.input()
        self.move()
        self.animate()

