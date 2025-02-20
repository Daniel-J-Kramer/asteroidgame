# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        player.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(6000) / 1000


if __name__ == "__main__":
    main()
