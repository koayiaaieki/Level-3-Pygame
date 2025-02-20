import pygame
from config import *
from image_handler import *

class Character(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        animation_frame = import_folder('assets/character/idle/')
        self.image = animation_frame[0]
        self.rect = self.image.get_rect(topleft=position)
        self.direction = {'x': 0, 'y': 0}
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()
        #y movement
        if keys[pygame.K_UP]:
            self.direction['y'] = -1
        elif keys[pygame.K_DOWN]:
            self.direction['y'] = 1
        else:
            self.direction['y'] = 0
        #x movement
        if keys[pygame.K_RIGHT]:
            self.direction['x'] = 1
        elif keys[pygame.K_LEFT]:
            self.direction['x'] = -1
        else:
            self.direction['x'] = 0

    def move(self):
        self.rect.centerx += self.direction['x'] * self.speed
        self.rect.centery += self.direction['y'] * self.speed

    def update(self):
        self.input()
        self.move()

