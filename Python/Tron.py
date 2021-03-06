from turtle import *
from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True if head inside screen."
    return -100 < head.x < 100 and -100 < head.y < 100

def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player green wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player blue wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'green')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(100), 'a')
onkey(lambda: p1aim.rotate(-100), 'd')
onkey(lambda: p2aim.rotate(100), 'j')
onkey(lambda: p2aim.rotate(-100), 'l')
draw()
done()


