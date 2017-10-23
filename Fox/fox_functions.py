#! python3 

import pygame
import sys

def check_events(fox):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,fox)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,fox)

def update_screen(screen,fox):
	screen.fill((0,0,230))
	fox.blitme()

    #Update Screen
	pygame.display.flip()

def check_keydown_events(event,fox):
	if event.key == pygame.K_RIGHT:
		fox.moving_right = True
		print(event.key)
	elif event.key == pygame.K_LEFT:
		fox.moving_left = True
		print(event.key)
	elif event.key == pygame.K_UP:
		fox.moving_up = True
		print(event.key)
	elif event.key == pygame.K_DOWN:
		fox.moving_down = True
		print(event.key)
def check_keyup_events(event,fox):
	if event.key == pygame.K_RIGHT:
		fox.moving_right = False
	elif event.key == pygame.K_LEFT:
		fox.moving_left = False
	elif event.key == pygame.K_UP:
		fox.moving_up = False
	elif event.key == pygame.K_DOWN:
		fox.moving_down = False
