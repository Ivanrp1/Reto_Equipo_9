from turtle import *
from random import randrange
from freegames import square, vector
"""
Code for Snake Game
"""
food = vector(0, 0)
snake = [vector(20, 0)]
aim = vector(0, -20)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 14, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 20
        food.y = randrange(-15, 15) * 20
    else:
        snake.pop(0)

    clear()

    for body in snake:
<<<<<<< HEAD
        square(body.x, body.y, 14, 'black')

    square(food.x, food.y, 14, 'green')
=======
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
>>>>>>> b0caac4a2b145594fce387d15d08e4ec922f94a7
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(20, 0), 'Right')
onkey(lambda: change(-20, 0), 'Left')
onkey(lambda: change(0, 20), 'Up')
onkey(lambda: change(0, -20), 'Down')
move()
done()
