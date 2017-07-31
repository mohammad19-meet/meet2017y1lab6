import turtle

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"
K_KEY = "k"
P_KEY = "p"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP


def up():
    global direction
    direction = UP
    print('Up Arrow')
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x, y+10)
    print(turtle.pos())
def left():
    global direction
    direction = LEFT
    print('Left Arrow')
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x-10,y)
def down():
    global direction
    direction = DOWN
    print('Down Arrow')
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x,y-10)
def right():
    global direction
    direction = RIGHT
    print('Right Arrow')
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x+10,y)
def pen_up():
    global direction
    direction = K_KEY
    print('Pen Up')
    turtle.penup()
def pen_down():
    global direction
    direction = P_KEY
    print('Pen Down')
    turtle.pendown()
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(turtle.stamp, SPACEBAR)
turtle.onkeypress(pen_up, K_KEY)
turtle.onkeypress(pen_down, P_KEY)
turtle.listen()
