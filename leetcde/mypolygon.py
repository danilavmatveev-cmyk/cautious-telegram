import fix_turtle  # импортируем первым!


import turtle
bob = turtle.Turtle()
print(bob)
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()