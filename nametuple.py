from collections import namedtuple

Color = namedtuple('Color',['red','green','blue'])

color = Color(55,155,255)
white=Color(255,255,255)
#print(color['red'])
print(color[1])

print(color.blue)

print(white.green)

print(white.red)
