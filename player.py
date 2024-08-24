from circleshape import CircleShape
from pygame import *
import pygame
import constants
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.position = Vector2(x, y)
        self.rotation = 0
        self.timer = 0


    # in the player class
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "crimson", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(dt * -1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt): 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer > 0: return
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity.scale_to_length(constants.PLAYER_SHOOT_SPEED)
        self.timer = 0.3
        