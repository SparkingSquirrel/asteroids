from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS #check if too small?
        if new_radius <= ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            v1 *= ASTEROID_SPLIT_ACCEL
            v2 *= ASTEROID_SPLIT_ACCEL
            child1 = Asteroid(self.position.x, self.position.y, new_radius)
            child2 = Asteroid(self.position.x, self.position.y, new_radius)
            child1.velocity = v1
            child2.velocity = v2
        self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity