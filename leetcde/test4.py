import fix_turtle
import turtle
def koch(t, length):
    if length < 3:
        t.fd(length)
    angle = 60
    t.fd(length/3)
    t.lt(angle)
    t.fd(length / 3)
    t.rt(2 * angle)
    t.fd(length / 3)
    t.lt(angle)



    turtle.mainloop()
if __name__ == '__main__':
    bob = turtle.Turtle()
koch(bob,150)