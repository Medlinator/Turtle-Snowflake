import turtle
import random

wn = turtle.Screen()
elsa = turtle.Turtle()
colors = ["cyan", "purple", "white", "blue"]

wn.bgcolor("grey")

def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

for i in range(8):
    # elsa.color(random.choice(colors))
    branch()
    elsa.left(45)
    
wn.exitonclick()



    
