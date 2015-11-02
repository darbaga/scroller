from collections import defaultdict
class Map(object):
    def __init__(self, default_tile, impassable_tile, min_x=0, max_x=100, min_y=0, max_y=5):
        self.min_x, self.min_y = min_x, min_y
        self.max_x, self.max_y = max_x, max_y
        self.default_tile, self.impassable_tile = default_tile, impassable_tile
        self._map = defaultdict(lambda: impassable_tile)
        self.generate_map()
    def get_tile(self, coordinates):
        return self._map[coordinates]
    def generate_map(self):
        #we add +1 to max because xrange does not give us the end value
        #if we just use max.
        for i in xrange(self.min_x, self.max_x+1):
            for j in xrange(self.min_y, self.max_y+1):
                self._map[(i, j)]=self.default_tile
    def is_impassable(self, coordinates):
        return self.get_tile(coordinates).impassable


class Tile(object):
    """the most basic object in a map.
        has a collide method which plays sound for type.
    """
    def __init__(self, sound, impassable=False):
        self.sound = sound
        self.impassable = impassable
    def collide(self, player):
        self.sound.play()
