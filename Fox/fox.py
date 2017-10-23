#! python3

import pygame

class Fox(): 
	def __init__(self,screen):
		'''Initialize the ship and set its starting position'''
		self.screen = screen

		# Load the ship image and get its rect
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen 
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

		# Moving Flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		#Get Center
		self.center = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 1
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 1 
		if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 1
		if self.moving_down and self.rect.top > 0: 
			self.rect.centery -= 1


	def blitme(self):
		# Draw the ship at the current location 
		self.screen.blit(self.image, self.rect)
