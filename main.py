import pygame
from constants import *
from player import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)			
	running = True
	clock = pygame.time.Clock()
	dt = 0	
	while running:
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill((0, 0, 0))
		p.draw(screen)
		pygame.display.flip()
	
if __name__ == "__main__":
	main()
