class Vector(object):
    __slots__=['x', 'y']
    
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x,y
    def __add__(self, other):
        return self.__class__(self.x+other.x, self.y+other.y)
    def scale(self, num):
        return self.__class__(self.x*num, self.y*num)
        
    def isint(self):
        return self.x.is_integer() and self.y.is_integer()
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)