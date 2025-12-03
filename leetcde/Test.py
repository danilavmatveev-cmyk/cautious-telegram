import fix_turtle  # импортируем первым!


import turtle
import math
bob = turtle.Turtle()


def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t,r):
    arc(t,r,360)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t,r,angle):
    arc_length = (r*math.pi*angle)/180
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length,step_angle)
    turtle.mainloop()

arc(bob,50,90)






