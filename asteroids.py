from circleshape import *
import random
from  constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.radius = radius

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius)			
	
	def update(self, dt):
		self.position += self.velocity * dt		 

	def split(self):
		self.kill()
		random_angle = random.uniform(20, 50)
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			vector_1 = self.velocity.rotate(random_angle)
			vector_2 = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			as_1 = Asteroid(self.position.x, self.position.y, new_radius)
			as_2 = Asteroid(self.position.x, self.position.y, new_radius)
			as_1.velocity = 1.2 * vector_1
			as_2.velocity = 1.2 * vector_2