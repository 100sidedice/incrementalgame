import sys
import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

square = pygame.Rect(100, 100, 50, 50)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        # the (255,0,0) is red
        pygame.draw.rect(screen, (255, 0, 0), square)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()