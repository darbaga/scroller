"""
This class holds game object classes
"""
class BaseGameObj(object):
    """Basic game object template"""
    def __init__(self, name='', description='', getsound='', dropsound='', affects=[])
        self.name=name
        self.description=description
        self.getsound=getsound
        self.dropsound=dropsound
        self.affects=affects

class Weapon(BaseGameObj):
    """Class for most weapons. If you need to add any more attributes / methods, just subclass / inherit this"""
    def __init__
        """This class is supposed to have everything BaseGameObj does, plus swingsound, equipSound, other weapon related things, with the self.swingsound=swingsound... Etc... COde added on the BaseGameObj's __init__ function."""