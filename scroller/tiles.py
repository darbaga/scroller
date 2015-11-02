class Tile(object):
    """the most basic object in a map."""
    def __init__(self, sound, impassable=False):
        self.sound = sound
        self.impassable = impassable
    def collide(self, player):
        self.sound.play()
