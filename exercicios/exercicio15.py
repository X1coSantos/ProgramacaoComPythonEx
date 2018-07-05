# ['DEFAULT_ANGLEOFFSET', 'DEFAULT_ANGLEORIENT', 'DEFAULT_MODE', 'START_ORIENTATION', '__class__', '__delattr__',
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cc', '_clear', '_clearstamp',
# '_color', '_colorstr', '_delay', '_drawturtle', '_getshapepoly', '_go', '_goto', '_newLine', '_pen', '_polytrafo',
# '_reset', '_rotate', '_screen', '_setDegreesPerAU', '_setmode', '_tracer', '_undo', '_undogoto', '_update',
# '_update_data', '_write', 'back', 'backward', 'begin_fill', 'begin_poly', 'bk', 'circle', 'clear', 'clearstamp',
# 'clearstamps', 'clone', 'color', 'degrees', 'distance', 'dot', 'down', 'end_fill', 'end_poly', 'fd', 'fillcolor',
# 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getpen', 'getscreen', 'getturtle', 'goto', 'heading', 'hideturtle',
# 'home', 'ht', 'isdown', 'isvisible', 'left', 'lt', 'onclick', 'ondrag', 'onrelease', 'pd', 'pen', 'pencolor', 'pendown',
# 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'reset', 'resizemode', 'right', 'rt', 'screens', 'seth',
# 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setx', 'sety', 'shape', 'shapesize',
# 'shapetransform', 'shearfactor', 'showturtle', 'speed', 'st', 'stamp', 'tilt', 'tiltangle', 'towards', 'turtlesize',
# 'undo', 'undobufferentries', 'up', 'width', 'write', 'xcor', 'ycor']


from turtle import Turtle

tess = Turtle()
distancia = 1

while True:
    tess.speed(10000000)
    tess.forward(distancia)
    tess.right(90)
    tess.forward(distancia)
    tess.right(90)
    tess.forward(distancia)
    tess.begin_fill()

    distancia = distancia * 1.6