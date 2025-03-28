from circleshape import *
from constants import PLAYER_SHOOT_SPEED, SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
	def __init__(self, x, y, radius, turn_speed, player_speed, shots):
		super().__init__(x, y, radius)	
		self.rotation = 0
		self.turn_speed = turn_speed
		self.player_speed = player_speed
		self.shots = shots
		self.shoot_timer = SHOOT_COOLDOWN
	# in the player class
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
		
	def rotate(self, dt):
		self.rotation += self.turn_speed * dt

	def update(self, dt):
		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(dt * -1)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_s]:
			self.move(dt * -1)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * self.player_speed * dt
	
	def shoot(self):
		self.shoot_timer = SHOOT_COOLDOWN
		new_shot = Shot(self.position.x, self.position.y)
		direction = pygame.Vector2(0, 1).rotate(self.rotation)
		new_shot.velocity = direction * PLAYER_SHOOT_SPEED
		self.shots.add(new_shot)