"""
This class holds game object classes
"""
class BaseGameObj(object):
    """Basic game object template"""
    def __init__(self, name='', description='', getsound='', dropsound='', effects=[], *args, **kwargs):
        if name == '' and description == '' and getsound == '' and dropsound == '' and effects == []:
            self.name, self.description = kwargs['name'], kwargs['description']
            self.getsound, self.dropsound = kwargs['getsound'], kwargs['dropsound']
            self.effects = kwargs['effects']
        else:
            self.name=name
            self.description=description
            self.getsound=getsound
            self.dropsound=dropsound
            self.effects=effects

class Weapon(BaseGameObj):
    """Class for most weapons. If you need to add any more attributes / methods, just subclass / inherit this"""
    def __init__(self, swingsound='', equipsound='', *args, **kwargs):
        super(Weapon, self).__init__(self, *args, **kwargs)
        """This class is supposed to have everything BaseGameObj does, plus swingsound, equipSound, other weapon related things, with the self.swingsound=swingsound... Etc... COde added on the BaseGameObj's __init__ function."""