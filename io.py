import pygame
import graphics

zoom_multiplier = 1.5
zoom_max = 16
zoom_min = 1


def respond_to_inputs(event, pressed, tempdata, world_object):
    if pressed[pygame.K_UP]:
        print "UP"
        tempdata['y_position'] -= 1
    #    if tempdata['y_position'] < 0:
      #    tempdata['y_position'] = 0
    if pressed[pygame.K_DOWN]:
        print "DOWN"
        tempdata['y_position'] += 1
      #  if tempdata['y_position'] > tempdata['y_max']:
      #    tempdata['y_position'] = tempdata['y_max']
    if pressed[pygame.K_LEFT]:
        print "LEFT"
        tempdata['x_position'] -= 1
      #  if tempdata['x_position'] < 0:
      #    tempdata['x_position'] = 0
    if pressed[pygame.K_RIGHT]:
        print "RIGHT"
        tempdata['x_position'] += 1
    #    if tempdata['x_position'] > tempdata['x_max']:
    #      tempdata['x_position'] = tempdata['x_max']
    if pressed[pygame.K_9]:
        print "ZOOM OUT"
        tempdata['zoom'] = tempdata['zoom'] * zoom_multiplier
        tempdata['map_object'] = graphics.regenerate_map(world_object, tempdata['zoom'])
    #    if tempdata['zoom'] > zoom_max:
    #      tempdata['zoom'] = zoom_max
    if pressed[pygame.K_0]:
        print "ZOOM IN"
        tempdata['zoom'] = tempdata['zoom'] / zoom_multiplier
        tempdata['map_object'] = graphics.regenerate_map(world_object, tempdata['zoom'])
      #  if tempdata['zoom'] < zoom_min:
      #    tempdata['zoom'] = zoom_min

    return tempdata
