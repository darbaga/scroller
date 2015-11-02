"""
This class holds game object classes
"""
class BaseGameObj(object):
    """Basic game object template"""
    def __init__(self, name='', description='', getsound='', dropsound='', effects=[]):
        self.name=name
        self.description=description
        self.getsound=getsound
        self.dropsound=dropsound
        self.effects=effects

class Weapon(BaseGameObj):
    """Class for most weapons. If you need to add any more attributes / methods, just subclass / inherit this"""
    def __init__(self, name='', description='', getsound='', dropsound='', effects=[], swingsound='', equipsound=''):
        super(Weapon, self).__init__(self, name=name, description=description, getsound=getsound, dropsound=dropsound, effects=effects)
        """This class is supposed to have everything BaseGameObj does, plus swingsound, equipSound, other weapon related things, with the self.swingsound=swingsound... Etc... COde added on the BaseGameObj's __init__ function."""