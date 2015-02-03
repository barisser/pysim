import pygame
import graphics
import map

def cycle(screen, world):
    #render_land(screen)
    graphics.draw(screen, world)
    
def game_init():
    return map.island_world()
