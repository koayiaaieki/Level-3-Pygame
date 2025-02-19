import pygame
from utilities.config import TILE_SIZE

class Image:
    def __init__(self, player):
        self.player = player
        # Surface
        self.image_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def animate(self):
        current_action = self.player.current_action
        self.player.frame_index += self.player.frame_speed
        if self.player.frame_index >= len(self.player.frames[current_action]):
            self.player.frame_index = 0
        self.frame_image = self.player.frames[current_action][int(self.player.frame_index)]

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))
        self.image_surface.set_colorkey("black")

    def update(self):
        self.animate()
        self.compose()
        self.player.image = self.image_surface
