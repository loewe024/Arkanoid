import pygame
from Ball import Ball
pygame.init()
a = Ball(200, 180, 20, [0, 255, 0], 5, 5)
# Set up the drawing window
screen = pygame.display.set_mode([600, 500])
width = 600
height = 500
clock = 0
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height), 1)
    # Draw a solid blue circle in the center
    a.draw_ball()
    clock += 1
    if a.xcoord >= width - 2 * a.radius:
        a.xvelo = -abs(a.xvelo)
    elif a.xcoord <= 0:
        a.xvelo = abs(a.xvelo)

    if a.ycoord >= height - 2 * a.radius:
        a.yvelo = -abs(a.yvelo)
    elif a.ycoord <= 0:
        a.yvelo = abs(a.yvelo)


    if clock % a.xvelo == 0 and a.xvelo > 0:
        a.xcoord += 1
    elif clock % a.xvelo == 0:
        a.xcoord -= 1

    if clock % a.yvelo == 0 and a.yvelo > 0:
        a.ycoord += 1
    elif clock % a.yvelo == 0:
        a.ycoord -= 1

    screen.blit(a.bildschirm, (a.xcoord, a.ycoord))
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()
