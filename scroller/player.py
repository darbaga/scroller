import pdb

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
        self.tile=self.map.get_tile((int(self.position.x), int(self.position.y)))
        
        self.KeyStateHandler=KeyStateHandler
        
        self.has_moved=False
        #(how many times the loop loops/how much tiles the player should be able to cover in a second)=
        self.move_counter=15
        
    def move(self, x, y):
        if self.map.get_tile((self.position.x+x, self.position.y+y)).impassable:
            self.map.get_tile((self.position.x+x, self.position.y+y)).collide(self)
        else:
            self.position=Vector(self.position.x+x, self.position.y+y)
    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT and self.move_counter==0:
            self.move(-1, 0)
            self.has_moved=True
        elif symbol==key.RIGHT and self.move_counter==0:
            self.move(1, 0)
            self.has_moved=True
        elif symbol == key.C:
            print(self.position)
        elif symbol == key.H:
            print("You have %d out of %d hp, (%d percent)." %(self.hp, self.max_hp, self.hp/self.max_hp*100))
        if symbol==key.M:
            print(self.move_counter)
        if symbol==key.P:
            pdb.set_trace()

    def update(self, dt):
        if self.has_moved:
            self.has_moved=False
            self.move_counter=15
        if self.move_counter>0:
            self.move_counter-=1
        if self.tile!=self.map.get_tile((int(self.position.x), int(self.position.y))):
            self.map.get_tile((int(self.position.x), int(self.position.y))).collide(self)
            self.tile=self.map.get_tile((int(self.position.x), int(self.position.y)))
        if self.KeyStateHandler.get(key.RIGHT, None)==True and self.move_counter==0:
            self.move(1, 0)
            self.has_moved=True
        if self.KeyStateHandler.get(key.LEFT, None)==True and self.move_counter==0:
            self.move(-1, 0)
            self.has_moved=True