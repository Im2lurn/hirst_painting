# from colorgram import extract
#
# colors_dict = extract("damien hirst dot painting img.jpg", 40)
# colors_rgb = []
# for _ in colors_dict:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     col = (r, g, b)
#     colors_rgb.append(col)

color_list = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32)]
from turtle import Screen, Turtle, colormode
import random

colormode(255)

timmy = Turtle()
timmy.speed(1500)
timmy.penup()
timmy.goto(-350,-300)

for __ in range(13):
    for _ in range(14):
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
    timmy.pendown()
    timmy.dot(20, random.choice(color_list))
    timmy.penup()

    if __ % 2 == 0:
        timmy.right(270)
        timmy.forward(50)
        timmy.right(270)
    else:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)



screen = Screen()
screen.exitonclick()