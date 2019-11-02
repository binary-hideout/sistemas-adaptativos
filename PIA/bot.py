import pygame
from pygame.sprite import Sprite
import math
import random

class Bot(Sprite):
    def __init__(self, screen, game_settings, population):
        super(Bot, self).__init__()
        self.health = 100
        self.speed = 1
        self.energy = 100
        self.damage = 20
        self.population = population
        self.screen = screen
        self.image = pygame.image.load('ship.bmp')
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #self.line = pygame.draw.line(screen, (0, 255, 0), (self.rect.x, self.rect.y), (self.rect.x + 50, self.rect.y + 50))
        self.rect.centerx = random.randint(1, 1000)
        self.rect.centery = random.randint(1, 500)
        self.moving_forward = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.game_settings = game_settings

    def angle(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        dx = self.mouse_x - self.rect.centerx
        dy = self.mouse_y - self.rect.centery
        return (180 / math.pi) * math.atan2(-dy, dx) - 90

    def check_movement(self):
        if self.moving_forward and self.rect.y > 0:
            self.rect.centery -= self.speed
            self.energy -= self.speed
        if self.moving_down and self.rect.y < self.game_settings.screen_height - self.rect.height:
            self.rect.centery += self.speed
            self.energy -= self.speed
        if self.moving_left and self.rect.x > 0:
            self.rect.centerx -= self.speed
            self.energy -= self.speed
        if self.moving_right and self.rect.x < self.game_settings.screen_width - self.rect.width:
            self.rect.centerx += self.speed
            self.energy -= self.speed

    def update_mouse(self):
        self.image = pygame.transform.rotozoom(self.image_clean, self.angle(), 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def check_health(self):
        width = (self.rect.width * self.health / 100)
        self.health_bar = pygame.Rect(0, 0, width, 10)

   #def check_nearby_enemies():

    def detect_collisions(self):
        if pygame.sprite.spritecollideany(self, self.population):
            print("Hit")

    #def kill(self):

    def update(self):
        self.check_health()
        self.update_mouse()
        self.check_movement()
    
    def blitme(self):
        pygame.draw.line(self.screen, (0, 255, 0), (self.rect.centerx, self.rect.centery), (self.mouse_x, self.mouse_y))
        pygame.draw.rect(self.image, (0, 255, 0), self.health_bar)
        self.screen.blit(self.image, self.rect)