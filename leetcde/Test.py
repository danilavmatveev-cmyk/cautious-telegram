import fix_turtle  # импортируем первым!


import turtle
import math
bob = turtle.Turtle()


def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
    print(t)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
    print(t)

def circle(t,r):
    circumference = 2*r*math.pi
    n = 360
    length = circumference/n
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
    print(t)


def arc(t,r,angle):
    length = (r*math.pi*angle)/180
    for i in range(angle):
        t.fd(length)
        t.lt(1)

arc(bob,1,360)


