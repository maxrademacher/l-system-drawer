from drawer import Drawer
from system import System

rules = {
    'X': 'F[-X][X]F[-X]+FX',
    'F': 'pFF'
}

s = System('X', rules)
d = Drawer(draw_speed=0, init_angle=0, init_size=7, fwd_amt=5, turn_amt=30, inc_amt=0.1)

d.draw(s.get_str(6))

try:
    input('any key to exit')
except:
    pass
