from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize with position and the SHOT_RADIUS constant
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
	    pygame.draw.circle(screen, "white", self.position, self.radius)			
    
    def update(self, dt):
        self.position += pygame.Vector2(self.velocity.x, self.velocity.y) * dt