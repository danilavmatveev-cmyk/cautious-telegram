import fix_turtle
import turtle

def koch(t, length):
    if length  < 3:
        t.fd(length)
    else:
        angle = 60
        koch(t, length/3)
        t.lt(angle)
        koch(t, length/3)
        t.rt(2 * angle)
        koch(t, length/3)
        t.lt(angle)
        koch(t, length/3)

if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.speed(0)

def snowflake():
    for i in range(3):
        koch(bob, 100)
        bob.rt(120)

    turtle.mainloop()

snowflake()