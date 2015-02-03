import pygame
import map
import main
import image_set
import math

map_screen_x_margin_left = 100
map_screen_y_margin_bottom = 100
map_screen_x_margin_right = 0
map_screen_y_margin_top = 0

world_map = -1
tilex = 141
tiley = 100

def draw_world_surface(surface, world_object):
    draw_terrain(surface, world_object)

def draw_terrain(surface, world_object):
    for x in range(world_object.mapx):
        for y in range(world_object.mapy):
            px = tilex*x
            py = tiley*y
            terrain_type = world_object.map[x][y].terrain
            img = image_set.terrain_colors[terrain_type]
            surface.blit(img, (px, py))

def draw(surface, world):
    draw_world_surface(surface, world)

def render_gridlines(screen, point_list, grid_color):
    pygame.draw.line(screen, grid_color, point_list[0], point_list[1], 1)
    pygame.draw.line(screen, grid_color, point_list[1], point_list[2], 1)
    pygame.draw.line(screen, grid_color, point_list[2], point_list[3], 1)
    pygame.draw.line(screen, grid_color, point_list[3], point_list[0], 1)

def render_terrain(screen, x, y, terrain_type, width, height, row):
    if terrain_type < len(image_set.terrain_colors):
        img = image_set.terrain_colors[terrain_type]
        screen.blit(img, (x, y))
        # color = map.land_colors[terrain_type]
        # point_list = flat_to_isometric_conversion(row, x, y, width, height)
        # pygame.draw.polygon(screen, color, point_list)
        # render_gridlines(screen, point_list, (200,30,30))
        #pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))


def render_world(screen, world_object):
    start_position_x = map_screen_x_margin_left
    end_position_x = main.screen_width - map_screen_x_margin_right
    start_position_y = map_screen_y_margin_top
    end_position_y = main.screen_height - map_screen_y_margin_bottom
    start_position = (start_position_x, start_position_y)

    total_width = end_position_x - start_position_x
    zone_width = total_width / (map.mapx+0.5)
    total_height = end_position_y - start_position_y
    zone_height = zone_width#total_height / map.mapy

    for x in range(world_object.mapx):
        for y in range(world_object.mapy):
            px = start_position_x + zone_width*x
            py = start_position_y + zone_height*y
            terrain_type = world_object.map[x][y].terrain
            render_terrain(screen, px, py, terrain_type, zone_width, zone_height, y)

#def render_city(screen, x, y, width, height):
