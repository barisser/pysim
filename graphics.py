import pygame
import map
import main
import image_set
import math

map_screen_x_margin_left = 100
map_screen_y_margin_bottom = 100
map_screen_x_margin_right = 0
map_screen_y_margin_top = 0

tilex = 142
tiley = 100


def map_init(world_object):
    width = world_object.mapx * tilex
    height = world_object.mapy * tiley
    world_map = pygame.Surface((width, height))
    return world_map


def regenerate_map(world_object, zoom):
    m = map_init(world_object)
    width = int(world_object.mapx*tilex / zoom)
    height = int(world_object.mapy*tiley / zoom)
    print width
    print height
    render_world(m, world_object)
    stretched_map = pygame.transform.smoothscale(m, (width, height))
    return stretched_map


def linear_to_hex_spacing(rowx, coly):
    y = coly * tiley /2
    if coly%2 == 0:
        x = rowx * tilex
    else:
        x = (rowx+0.5) * tilex
    return (x, y)


def draw_world_surface(surface, world_object):
    draw_terrain(surface, world_object)


def draw_terrain(surface, world_object):
    for x in range(world_object.mapx):
        for y in range(world_object.mapy):
            point = linear_to_hex_spacing(x, y)
            terrain_type = world_object.map[x][y].terrain
            img = image_set.terrain_colors[terrain_type]
            surface.blit(img, point)


def update_map(map_screen, world):
    draw_world_surface(map_screen, world)


def draw(screen, world, temp_data):
    x = temp_data['x_position']
    y = temp_data['y_position']
    map_screen = temp_data['map_object']
    position_map(map_screen, screen, temp_data['zoom'], temp_data['x_position'], temp_data['y_position'])


def position_map(map_surface, screen, zoom, x, y):
    px = x * tilex
    py = y * tiley
    p = (px, py)
    width = int(map_surface.get_width() / zoom)
    height = int(map_surface.get_height() / zoom)
    map_view_width = main.screen_width - map_screen_x_margin_right - map_screen_x_margin_left
    map_view_height = main.screen_height - map_screen_y_margin_top - map_screen_y_margin_bottom
    #screen.blit(stretched_map, (map_screen_x_margin_left, map_screen_y_margin_top), (px, py, map_view_width, map_view_height))
    screen.blit(map_surface, (map_screen_x_margin_left, map_screen_y_margin_top), (px, py, map_view_width, map_view_height))


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
