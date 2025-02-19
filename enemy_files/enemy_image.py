import pygame
from utilities.config import TILE_SIZE

class Image:
    def __init__(self, enemy):
        self.enemy = enemy
        # Surface
        self.image_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def animate(self):
        current_action = self.enemy.current_action
        self.enemy.frame_index += self.enemy.frame_speed
        if self.enemy.frame_index >= len(self.enemy.frames[current_action]):
            self.enemy.frame_index = 0
        self.frame_image = self.enemy.frames[current_action][int(self.enemy.frame_index)]

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))
        self.image_surface.set_colorkey("black")

    def update(self):
        self.animate()
        self.compose()
        self.enemy.image = self.image_surface
