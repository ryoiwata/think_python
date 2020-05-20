import turtle

Leonard = turtle.Turtle()



def polygon(t, sides=3, length=100):
    for num in range(sides):
        t.fd(length)
        t.rt(360/sides)

polygon(Leonard, sides=15)


