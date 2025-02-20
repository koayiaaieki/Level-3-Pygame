import pygame
from config import *
from image_handler import get_all_frames, flip_frames

class Character(pygame.sprite.Sprite):
    def __init__(self, position, groups, dict):
        super().__init__(groups)
        self.animation_frame = get_all_frames(dict)
        
        #idle frame doesnt need to flip
        self.animation_frame.update({"idle_left":flip_frames(self.animation_frame["idle_right"])})
        #walk frames do need to flip
        self.animation_frame.update({"walk_left":flip_frames(self.animation_frame["walk_right"])})

        self.image = self.animation_frame["idle_right"][0]
        self.rect = self.image.get_rect(topleft = position)

        #move
        self.direction_vector = {'x': 0, 'y': 0}
        self.speed = 5

        # fraem
        self.frame_index = 0
        self.frame_rate = 0.2

        #action
        self.action = "idle"
        self.direction = "right"
        self.current_action = f"{self.action}"
    
    def decide_action(self):
        if self.direction_vector['x'] != 0 or self.direction_vector['y'] != 0:
            action = "walk"
            self.frame_rate = 0.2
        else:
            action = "idle"

        self.action = action

    def decide_direction(self):
        keys = pygame.key.get_pressed()
        #y
        if keys[pygame.K_UP]:
            self.direction_vector['y'] = -1
            self.direction = "right"
        elif keys[pygame.K_DOWN]:
            self.direction_vector['y'] = 1
            self.direction = "right"
        else:
            self.direction_vector['y'] = 0
        #x
        if keys[pygame.K_RIGHT]:
            self.direction_vector['x'] = 1
            self.direction = "right"
        elif keys[pygame.K_LEFT]:
            self.direction_vector['x'] = -1
            self.direction = "left"
        else:
            self.direction_vector['x'] = 0

    def decide_current_action(self):
        self.decide_action()
        self.decide_direction()
        self.current_action = f"{self.action}_{self.direction}"
    
    def move(self):
        self.rect.centerx += self.direction_vector['x'] * self.speed
        self.rect.centery += self.direction_vector['y'] * self.speed

    def animate(self):
        self.frame_index += self.frame_rate
        if self.frame_index >= len(self.animation_frame[self.current_action]):
            self.frame_index = 0
        self.image = self.animation_frame[self.current_action][int(self.frame_index)]

    def update(self):
        self.decide_current_action()
        self.move()
        self.animate()

#note for top and down direction for sprites; current sprite_sheet doesnt have those directions yet but placeholder for now (will change later)