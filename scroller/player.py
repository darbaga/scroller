from pyglet.window import key
class Player(object):
    def __init__(self, map):
        self.map = map
        self.position = [0, 0]
    def move_left(self):
        #our player has a list of position coordinates, while our map expects a tuple.
        if self.map.is_impassable((self.position[0]-1, self.position[1])):
            self.map.get_tile((self.position[0]-1, self.position[1])).collide(self)
        else:
            self.map.get_tile((self.position[0]-1, self.position[1])).collide(self)
            self.position[0]-=1
    def move_right(self):
        if self.map.is_impassable((self.position[0]+1, self.position[1])):
            self.map.get_tile((self.position[0]+1, self.position[1])).collide(self)
        else:
            self.map.get_tile((self.position[0]+1, self.position[1])).collide(self)
            self.position[0]+=1
    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.move_left()
        elif symbol==key.RIGHT:
            self.move_right()
        elif symbol == key.C:
            print self.position
