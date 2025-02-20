# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(x, y, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)
        drawable.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(6000) / 1000


if __name__ == "__main__":
    main()