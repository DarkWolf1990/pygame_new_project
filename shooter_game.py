import sys

import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen_fill_color = (72, 61, 139)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

FIGHTER_STEP = 0.5

fighter_image = pygame.image.load('img/spaceShip.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height

fighter_is_moving_left, fighter_is_moving_right = False, False

RACKET_STEP = 0.3
rocket_image = pygame.image.load('img/ball.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_X, rocket_y = fighter_x + fighter_width / 2 - rocket_width / 2, fighter_y - rocket_height
rocket_was_fired = False

pygame.mixer.music.load('music/bensound-lofinerdbassbuzzer.mp3')
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True

            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_X = fighter_x + fighter_width / 2 - rocket_width / 2
                rocket_y = fighter_y - rocket_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False
    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False
    if rocket_was_fired:
        rocket_y -= RACKET_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_X, rocket_y))
    pygame.display.update()

