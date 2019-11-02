import sys
import math
import pygame
from pygame.sprite import Group
from settings import Settings
from bot import Bot
import game_functions as gf

def main():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Simulation')
    population = Group()
    spaceship = Bot(screen, game_settings, population)
    spaceship2 = Bot(screen, game_settings, population)
    population.add(spaceship)
    population.add(spaceship2)

    while True:
        gf.check_events(screen, population)
        population.update()  
        gf.update_screen(screen, game_settings, population)

if __name__ == '__main__': main()