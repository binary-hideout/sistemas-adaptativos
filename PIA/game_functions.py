import sys
import math
import pygame

def check_keydown_events(event, screen, bot):
    if event.key == pygame.K_UP:
        bot.moving_forward = True
    elif event.key == pygame.K_DOWN:
        bot.moving_down = True
    elif event.key == pygame.K_LEFT:
        bot.moving_left = True
    elif event.key == pygame.K_RIGHT:
        bot.moving_right = True
    #elif event.key == pygame.K_SPACE:
        #bot.attack()

def check_keyup_events(event, bot):
    if event.key == pygame.K_UP:
        bot.moving_forward = False
    elif event.key == pygame.K_DOWN:
        bot.moving_down = False
    elif event.key == pygame.K_LEFT:
        bot.moving_left = False
    elif event.key == pygame.K_RIGHT:
        bot.moving_right = False

def check_events(screen, population):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            for bot in population.sprites():
                if event.type == pygame.KEYDOWN:
                    check_keydown_events(event, screen, bot)
            
                elif event.type == pygame.KEYUP:
                    check_keyup_events(event, bot)

def update_screen(screen, game_settings, population):
    screen.fill(game_settings.bg_color)
    population.draw(screen)
    pygame.display.flip()
