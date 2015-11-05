from pyglet.window import key

from vector import Vector

class Player(object):
    """Holds player related data. 
        X is position on x axis, or left / right
        Y is position on the y axis, or up and down.
        Max hp is the maximum hp a player can have, by default that's their current hp.
    """
    def __init__(self, map, KeyStateHandler, name='bob', max_hp=100):
        self.name=name
        self.max_hp=max_hp
        self.hp=self.max_hp
        
        self.map = map
        self.position = Vector()
        
        self.left_counter = 0
        self.right_counter = 0
        self.KeyStateHandler = KeyStateHandler
        
    def move_left(self):
        #our player has a list of position coordinates, while our map expects a tuple.
        if self.map.is_impassable((self.position.x-1, self.position.y)):
            self.map.get_tile((self.position.x-1, self.position.y)).collide(self)
        else:
            self.map.get_tile((self.position.x-1, self.position.y)).collide(self)
            self.position.x-=1
    def move_right(self):
        if self.map.is_impassable((self.position.x+1, self.position.y)):
            self.map.get_tile((self.position.x+1, self.position.y)).collide(self)
        else:
            self.map.get_tile((self.position.x+1, self.position.y)).collide(self)
            self.position.x+=1
    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.left_counter+=50
        elif symbol==key.RIGHT:
            self.right_counter+=50
        elif symbol == key.C:
            print self.position
        elif symbol == key.H:
            print "You have %d out of %d hp, (%d percent)." %(self.hp, self.max_hp, self.hp/self.max_hp*100)

    def update(self, dt):
        if self.left_counter>300:
            self.move_left()
            self.left_counter = 0
        elif self.right_counter>300:
            self.move_right()
            self.right_counter = 0
        elif self.KeyStateHandler[key.RIGHT]:
            self.right_counter+=50
        elif self.KeyStateHandler[key.LEFT]:
            self.left_counter += 50
