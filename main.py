import pygame
import gamelogic

screen_width = 800
screen_height = 600
frame_rate = 60

def init():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    gamelogic.graphics.image_set.init()
    return screen

def main_loop():
    clock = pygame.time.Clock()
    screen = init()

    map_surface = pygame.surface

    done = False

    world = gamelogic.game_init()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))
        gamelogic.cycle(screen, world)

        pygame.display.flip()
        clock.tick(frame_rate)

if __name__ == '__main__':
    main_loop()
