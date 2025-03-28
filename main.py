import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import * 

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	# Initialize display and game objects
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids")

	
	# Create sprite groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable)

	

	
	# Create player
	p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, shots)
	
	#Create AsteroidField 
	af = AsteroidField()
	# Game loop setup
	running = True
	clock = pygame.time.Clock()
	dt = 0

	# Main game loop
	while running:
		# Time management
		dt = clock.tick(60) / 1000
		
		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
		
		# Update game state
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collide(p):
				print("Game Over")
				pygame.quit()
			
			for bullet in shots:
				if asteroid.collide(bullet):
					asteroid.split()
					bullet.kill()
			

		
		# Render
		screen.fill((0, 0, 0))
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
	
	# Cleanup
	pygame.quit()

if __name__ == "__main__":
	main()
