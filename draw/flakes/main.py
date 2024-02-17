import turtle
import random

#def shuriken():
#for i in range(10):
#    for i in range(2):
#        pat.forward(100)
#        pat.right(60)
#        pat.forward(100)
#        pat.right(120)
#    pat.right(36)

def branch():
    for i in range(3):
        for i in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)


pat = turtle.Turtle()
colours=["cyan","yellow","white"]
fond=["red","grey","black"]
turtle.Screen().bgcolor(random.choice(fond))
pat.color(random.choice(colours))
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()
for i in range(8):
    branch()
    pat.left(45)