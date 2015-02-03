import random
import math

land_colors = {}
land_colors[0] = (0,0,255)
land_colors[1] = (50, 200, 10)

mapy = 20
mapx = 10

class World:
    def __init__(self, mapx, mapy):
        self.map = []
        for i in range(mapx):
            r=[]
            for a in range(mapy):
                newland = Land()
                r.append(newland)
            self.map.append(r)
        self.mapx = mapx
        self.mapy = mapy


class Land:
    def __init__(self):
        #starts out formless
        self.terrain = 0
        self.altitude = 0
        self.resources = []
        self.cities = []

def blank_world():
    return World(mapx, mapy)

def island_world():
    w = World(mapx, mapy)
    w = islands(w)
    return w

def plains_world():
    w = World(mapx, mapy)
    for x in range(w.mapx):
        for y in range(w.mapy):
            w.map[x][y].terrain = 1
    return w

def islands(world):
    for x in range(world.mapx):
        for y in range(world.mapy):
            dx = int((x-world.mapx/2))
            dy = int((y-world.mapy/2))
            d = math.pow(dx*dx+dy*dy, 0.5)
            f = math.sin(d/3)
            if f>0.7:
                world.map[x][y].terrain=1
    return world
