from drawer import Drawer
from system import System

rules = {
    'X': 'F[-X][X]F[-X]+FX',
    'F': 'FF'
}

s = System('X', rules)
d = Drawer(0, 60, 3, 25)

d.draw(s.get_str(6))

try:
    input('any key to exit')
except:
    pass
