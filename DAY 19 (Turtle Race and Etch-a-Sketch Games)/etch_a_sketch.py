from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def go_forward():
    tim.forward(10)


def go_backward():
    tim.backward(10)


def turn_right():
    tim.right(20)


def turn_left():
    tim.left(20)


def clear():
    screen.resetscreen()
    tim.home()


screen.listen()
screen.onkeypress(key='w', fun=go_forward)
screen.onkeypress(key='s', fun=go_backward)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='a', fun=turn_left)

screen.onkey(key='x', fun=clear)

screen.exitonclick()
