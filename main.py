import pygame
import sys
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) 
        player.timer -= dt

        for sprite in asteroids:
            if sprite.collision_check(player):
                sys.exit("Game over!") 

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        #limit framerate to 60fps 
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
