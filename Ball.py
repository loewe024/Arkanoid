import pygame
import math
class Ball:
    xcoord = 0
    ycoord = 0
    radius = 0
    color = [0, 0, 0]
    xvelo = 0
    yvelo = 0
    bildschirm = pygame.Surface((2 * radius, 2 * radius))
    edge = []

    def __init__(self, x = 0, y = 0, r = 0, col = [0, 0, 0], xv = 0, yv = 0):
        self.xcoord = x
        self.ycoord = y
        self.radius = r
        self.color = col
        self.xvelo = xv
        self.yvelo = yv
        self.bildschirm = pygame.Surface((2 * self.radius, 2 * self.radius))
        for i in range (1001):
            self.edge.append([self.radius * math.cos(2 * math.pi * i / 1000), self.radius * math.sin(2 * math.pi * i / 1000)])

    def draw_ball(self):
        self.bildschirm.fill((255, 255, 255))
        pygame.draw.circle(self.bildschirm, self.color, (self.radius, self.radius), self.radius)

    def collision_player(self, xplayleft = 0, xplayright = 0, yplayup = 0, yplaydown = 0):
        invert = False
        weird = False
        weird = False
        for pair in self.edge:
            if xplayleft + 2 <= pair[0] + self.xcoord + self.radius <= xplayright - 2 and yplayup == pair[1] + self.ycoord + self.radius:
                invert = True
            if xplayleft + 1 >= pair[0] + self.xcoord + self.radius >= xplayleft - 1 and yplayup + 3 >= pair[1] + self.ycoord + self.radius >= yplayup:
                weird = True
                if self.xvelo <= 0:
                    weird = False
                    invert = True
            if xplayright + 1 >= pair[0] + self.xcoord + self.radius >= xplayright - 1 and yplayup + 3 >= pair[1] + self.ycoord + self.radius >= yplayup:
                weird = True
                if self.xvelo >= 0:
                    weird = False
                    invert = True
        if invert:
            self.yvelo = - self.yvelo
        if weird:
            self.yvelo = - self.yvelo
            self.xvelo = - self.xvelo