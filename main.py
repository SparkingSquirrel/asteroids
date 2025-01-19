# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys


def main():
    # print('Starting asteroids!') #not sure if instructions meant to remove these
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print('Game over!')
                sys.exit()

        screen.fill((0, 0, 0)) 
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()