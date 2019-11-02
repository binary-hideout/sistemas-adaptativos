import pygame
from pygame.sprite import Sprite

class Food(Sprite):
    def __init__(self, screen, bot):
        super(Food, self).__init__()
        self.screen = screen
        self.energy = 10
        self.food_width = 5
        self.food_height = 5
        self.food_color = (0, 0, 255)
        self.rect = pygame.Rect(0, 0, self.food_width, self.food_height)
