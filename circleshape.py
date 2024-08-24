import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else: 
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius 

    def draw(self, screen):
        pass 

    def update(self, dt):
        pass

    def collides(self, o):
        return self.position.distance_to(o.position) < (self.radius + o.radius)