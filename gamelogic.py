import pygame
import graphics
import map

def cycle(screen, world, tempdata):
    #render_land(screen)
    graphics.draw(screen, world, tempdata)

def game_init():
    return map.island_world()

def temp_init(world_object):
    tempdata = {}
    tempdata['x_position'] = 0
    tempdata['y_position'] = 0
    tempdata['x_max'] = world_object.mapx
    tempdata['y_max'] = world_object.mapy
    tempdata['zoom'] = 8
    tempdata['map_object'] = graphics.regenerate_map(world_object, tempdata['zoom'])

    return tempdata
