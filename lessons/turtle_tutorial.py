from turtle import Turtle, colormode, done
colormode(255)
side_length: int = 300


leo: Turtle = Turtle()
leo.color((255, 51, 93), (255, 213, 51))
leo.speed(4)
leo.hideturtle()
leo.up()
leo.goto(-150, -150)
leo.down()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()
bob.pencolor("Black")
bob.speed(12)
bob.hideturtle()
bob.up()
bob.goto(-150, -150)
bob.down()

counter: int = 0
while counter < 120:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
    counter += 1
done()