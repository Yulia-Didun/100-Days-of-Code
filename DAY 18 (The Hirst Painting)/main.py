# import colorgram      # extracts colors from image
# colors = colorgram.extract('image.jpg', 25)
# rgb_colors = []
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)

import random
import turtle
from turtle import Turtle, Screen

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (166, 204, 202), (62, 26, 45),
              (145, 165, 181), (6, 79, 111)]

turtle.colormode(255)

spot = Turtle()
spot.penup()
spot.hideturtle()
spot.speed('fastest')

spot.setheading(225)
spot.forward(350)
spot.setheading(0)
start_position = list(spot.pos())


def dots_line():
    """Draw line with 10 dots."""
    for _ in range(10):
        spot.dot(20, random.choice(color_list))
        spot.forward(50)


for line in range(10):
    start_position[1] += 50
    spot.setpos(start_position[0], start_position[1])
    dots_line()

screen = Screen()
screen.exitonclick()
