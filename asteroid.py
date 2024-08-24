import pygame
import random 
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS): return

        rand_angle = random.uniform(20, 50)
        a1 = self.velocity.rotate(rand_angle) * 1.2
        a2 = self.velocity.rotate(rand_angle * -1) * 1.2
        # a1.scale_to_length(1.2)
        # a2.scale_to_length(1.2)
        rad =  self.radius - ASTEROID_MIN_RADIUS
        
        as1 = Asteroid(self.position.x, self.position.y, rad)
        as2 = Asteroid(self.position.x, self.position.y, rad)
        
        as1.velocity = a1
        as2.velocity = a2
