import pygame
class Ball:
    xcoord = 0
    ycoord = 0
    radius = 0
    color = [0, 0, 0]
    xvelo = 0
    yvelo = 0
    bildschirm = pygame.Surface((2 * radius, 2 * radius))

    def __init__(self, x = 0, y = 0, r = 0, col = [0, 0, 0], xv = 0, yv = 0):
        self.xcoord = x
        self.ycoord = y
        self.radius = r
        self.color = col
        self.xvelo = xv
        self.yvelo = yv
        self.bildschirm = pygame.Surface((2 * self.radius, 2 * self.radius))

    def draw_ball(self):
        self.bildschirm.fill((255, 255, 255))
        pygame.draw.circle(self.bildschirm, self.color, (self.radius, self.radius), self.radius)

    def collision_player(self, xplayleft = 0, xplayright = 0, yplay = 0):
        if self.ycoord + 2 * self.radius == yplay and xplayleft <= self.xcoord + self.radius <= xplayright:
            self.yvelo = - self.yvelo