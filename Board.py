import pygame
from Ball import Ball
from Player import Player


pygame.init()
ball = Ball(200, 180, 20, [0, 255, 0], 1, 1)
player = Player(250, 450, 100, 10, [0, 0, 0], 0)
# Set up the drawing window
screen = pygame.display.set_mode([600, 500])
width = 600
height = 500


# Run until the user asks to quit
running = True
while running:

    clock = pygame.time.Clock()
    clock.tick(1000)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    ball.draw_ball()
    if ball.xcoord >= width - 2 * ball.radius:
        ball.xvelo = -abs(ball.xvelo)
    elif ball.xcoord <= 0:
        ball.xvelo = abs(ball.xvelo)

    if ball.ycoord >= height - 2 * ball.radius:
        ball.yvelo = -abs(ball.yvelo)
    elif ball.ycoord <= 0:
        ball.yvelo = abs(ball.yvelo)



    if ball.xvelo > 0:
        ball.xcoord += 1
    else:
        ball.xcoord -= 1

    if ball.yvelo > 0:
        ball.ycoord += 1
    else:
        ball.ycoord -= 1

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    if player.xcoord > width - player.width:
        player.xcoord = width - player.width
    if player.xcoord < 0:
        player.xcoord = 0
    player.draw_player()

    ball.collision_player(player.xcoord, player.xcoord + player.width, player.ycoord)

    screen.blit(ball.bildschirm, (ball.xcoord, ball.ycoord))
    screen.blit(player.bildschirm, (player.xcoord, player.ycoord))
    pygame.display.flip()

    # if ball.ycoord + 2 * ball.radius >= height:
    #     running = False
# Done! Time to quit.
pygame.quit()
