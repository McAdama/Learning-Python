import pygame
import sys
from fox import Fox
import fox_functions as ff 


def run_game():
	# Initialize game,settings and create screen object
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Blue Sky")

	bg_color = (0,0,230)

    # Make a fox
	fox = Fox(screen)

    # Start the main loop for the game
	while True:
		# Event Checker
		ff.check_events(fox)
		fox.update()
		ff.update_screen(screen,fox)

        # Fill screen
		screen.fill(bg_color)
		fox.blitme()
        # Make the most recently drawn screen visible
		pygame.display.flip()


run_game()
