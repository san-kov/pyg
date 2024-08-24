import sys
import pygame 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroidField = AsteroidField()

  


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        val = clock.tick(60)
        dt = val / 1000
        screen.fill("black")

        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)

        for i in asteroids:
            if i.collides(player):
                print("Game over")
                sys.exit()

            for s in shots:
                if s.collides(i): 
                    s.kill()
                    i.split() 

        pygame.display.flip()

   



if __name__ == "__main__":
    main()