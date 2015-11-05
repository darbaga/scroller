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
        
        self.is_moving=False
        self.movement_direction=Vector()
        self.movement_speed=3.0
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.is_moving=True
            self.movement_direction.x=-1
        elif symbol==key.RIGHT:
            self.is_moving=True
            self.movement_direction.x=1
        if modifiers & key.MOD_CTRL:
            self.movement_speed=5
        elif symbol == key.C:
            print self.position
        elif symbol == key.H:
            print "You have %d out of %d hp, (%d percent)." %(self.hp, self.max_hp, self.hp/self.max_hp*100)
            
    def on_key_release(self, symbol, modifiers):
        if symbol==key.LEFT or symbol==key.RIGHT:
            self.is_moving=False
        if modifiers & key.MOD_CTRL:
            self.movement_speed=3
    def update(self, dt):
        if self.is_moving:
            self.position=self.position+self.movement_direction.scale(self.movement_speed*dt)
        if self.tile!=self.map.get_tile((int(self.position.x), int(self.position.y))):
            if not self.map.get_tile((int(self.position.x), int(self.position.y))).impassable:
                self.map.get_tile((int(self.position.x), int(self.position.y))).collide(self)
                self.tile=self.map.get_tile((int(self.position.x), int(self.position.y)))
            else:
                self.map.get_tile((int(self.position.x), int(self.position.y))).collide(self)
        if not self.is_moving and self.position.x<int(self.position.x)+.5:
            self.position.x=int(self.position.x)+.5
        if self.position.x>self.map.max_x:
            self.position.x=self.map.max_x
