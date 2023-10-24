#Marissa Jones
# 10-24-23
# Turtle Import

import turtle

def draw_filled_polygon(sides, length, outline_color, fill_color):
    angle = 360 / sides

    turtle.color(outline_color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()

num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of the side: "))
outline_color = input("Enter the outline color: ")
fill_color = input("Enter the fill color: ")

screen = turtle.Screen()
screen.bgcolor("white")

polygon_turtle = turtle.Turtle()

polygon_turtle.penup()
polygon_turtle.pendown()

draw_filled_polygon(num_sides, side_length, outline_color, fill_color)
turtle.exitonclick()