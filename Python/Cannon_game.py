from random import randrange
from turtle import *
from freegames import vector

ball = vector(-150, -150)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -149
        ball.y = -149
        speed.x = (x + 150) / 25
        speed.y = (y + 150) / 25

def inside(xy):
    "Return True if xy within screen."
    return -150 < xy.x < 150 and -1500 < xy.y < 150

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'green')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 2,'blue')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(150, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
