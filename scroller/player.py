from pyglet.window import key
class Player(object):
    """Holds player related data. 
        X is position on x axis, or left / right
        Y is position on the y axis, or up and down.
        Max hp is the maximum hp a player can have, by default that's their current hp.
    """
    def __init__(self, name='bob', max_hp=100, map):
        self.name=name
        self.max_hp=max_hp
        self.hp=self.max_hp
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
        elif symbol == key.H:
            print "You have %d out of %d hp, (%d percent)." %(self.hp, self.max_hp, self.hp/self.max_hp*100)
