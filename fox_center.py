#! python3

import pygame

class Fox(): 
    def __init__(self,screen):
        '''Initialize the ship and set its starting position'''
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('fox.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        # Draw the ship at the current location 
        self.screen.blit(self.image, self.rect)