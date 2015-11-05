import pyglet

import libaudioverse
libaudioverse.initialize()
s = libaudioverse.Simulation()
s.set_output_device(-1)

from map import Map, Tile
from player import Player

from sound import SoundLoader
sounds = SoundLoader(s)

impassable_tile = Tile(sound=sounds.load_sound('impassable'), impassable=True)

Window = pyglet.window.Window()

keys = pyglet.window.key.KeyStateHandler()
Window.push_handlers(keys)

map = Map(lambda: Tile(sound=sounds.load_sound('default')), impassable_tile)

player = Player(map, keys)
Window.push_handlers(player)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(player.update, 1/60.0)
    pyglet.app.run()