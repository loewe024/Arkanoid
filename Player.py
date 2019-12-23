import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

class Player(pygame.sprite.Sprite):
    xcoord = 0
    ycoord = 0
    velo = 0
    width = 0
    height = 0
    color = [0, 0, 0]
    bildschirm = pygame.Surface((width, height))
    def __init__(self, x = 0, y = 0, w = 0, h = 0, col = [0, 0, 0], v = 0):
        self.xcoord = x
        self.ycoord = y
        self.velo = v
        self.width = w
        self.height = h
        self.color = col
        self.bildschirm = pygame.Surface((self.width, self.height))

    def draw_player(self):
        self.bildschirm.fill(self.color)

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.xcoord -= 1
        if pressed_keys[K_RIGHT]:
            self.xcoord += 1
