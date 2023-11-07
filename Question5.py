#Marissa Jones
#11-7-2023

#Lab Activity Module 7

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()

alex.color('blue')

side = 20
width = 10
for squares in range(5):

    drawSquare(alex,side)
    alex.penup()
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width
wn.exitonclick()