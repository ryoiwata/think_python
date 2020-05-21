import turtle
import math

def polygon(t, sides=3, length=100):
    for num in range(sides):
        t.fd(length)
        t.rt(360/sides)

def polyline(t, n=3, length=100, angle=60):
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def arc(t, r=100, angle=90):
    arc_length= 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def flower(t, petals=6, ratio=0.125):
    for num in range(petals):
        arc(t, angle= 360 * ratio)
        t.lt(180 - 360 * ratio)
        arc(t, angle= 360 * ratio)
        t.lt(180 / petals)


Leonard = turtle.Turtle()

flower(Leonard, petals = 64, ratio=0.125)

