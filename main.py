import sys
import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()