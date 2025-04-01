import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.timer = 0
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        player.timer -= dt

        for asteroid in asteroids:
            collision = player.collision(asteroid)
            if collision:
                sys.exit("Game Over!")

        for asteroid in asteroids:
            for shot in shots:
                collision = asteroid.collision(shot)
                if collision:
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
    main()
