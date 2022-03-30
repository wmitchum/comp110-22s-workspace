"""This will produce a picture of a quaint little house."""

__author__ = "730329770"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    oogway: Turtle = Turtle()
    square(oogway, -125, 125, 250, 240, 228, 138)  # Make x -(sides/2) and make y (sides/2). This will ensure a centered and proportional house. 
    roof(oogway, -125, 125, 250)  # Remember you must use the same numbers as in the function above to draw the house properly.
    windows(oogway, -125, 125, 250, 255, 255, 255)  # Use 255 for R, G, and B to make the windows white.
    window_hashes(oogway, -125, 125, 250)  # Again, use the same numbers.
    door(oogway, -125, 125, 250, 170, 77, 8)  # Continue to use the same numbers.
    doorknob(oogway, -125, 125, 250, 255, 235, 34)  # Continue to use the same numbers.


def square(a_turtle: Turtle, x: float, y: float, sides: float, R: int, G: int, B: int) -> None:
    """This function will draw the house sides and windows."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)  # This directs the turtle to orient itself right down the x-axis moving in the positive direction. 
    a_turtle.fillcolor(R, G, B)  # This allows the fill color to be flexible so we can use this function in another place.
    a_turtle.pensize(2)
    a_turtle.down()
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(sides)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def roof(a_turtle: Turtle, x: float, y: float, sides: float) -> None:
    """This function will trace out the roof of the house."""
    a_turtle.up()
    a_turtle.goto((x * 1.25), y)  # In order for the roof to be properly drawn, it's starting coordinates must be the same as those for square(). We multiply by 1.25 to make the roof slightly longer.
    a_turtle.setheading(90.0)
    a_turtle.color((159, 49, 11), (252, 84, 84))
    a_turtle.pensize(3)
    a_turtle.down()
    a_turtle.begin_fill()
    i: int = 0
    while i < 2:
        a_turtle.right(60)
        a_turtle.forward(sides * 0.57735 * 1.25)  # I got this number using a bit of trig -> it will make the sides the proper size if you use the side length of the large square.
        i += 1    
    a_turtle.setheading(180.0)
    a_turtle.forward(sides * 1.25)
    a_turtle.end_fill()


def windows(a_turtle: Turtle, x: float, y: float, sides: float, R: int, G: int, B: int) -> None:  # Use the same numbers as used for original large square.
    """This function will draw windows."""
    a_turtle.pencolor("black")
    square(a_turtle, (x + sides * 0.2), (y - sides * 0.2), (sides * .2), R, G, B)
    square(a_turtle, (x + sides * 0.6), (y - sides * 0.2), (sides * .2), R, G, B)


def window_hashes(a_turtle: Turtle, x: float, y: float, sides: float) -> None:  # Be sure to use the same coordinates and side length as the original large square.
    """This functions draws the hashes prominent in cartoon windows."""
    a_turtle.pencolor("black")
    a_turtle.pensize(2)

    a_turtle.up()  # The first part of this function will draw hashes for the left window.
    a_turtle.goto((x + sides * 0.3), (y - sides * 0.2))
    a_turtle.setheading(270.0)
    a_turtle.down()
    a_turtle.forward(sides * 0.2)
    a_turtle.up()
    a_turtle.goto((x + sides * 0.2), (y - sides * 0.3))
    a_turtle.setheading(0.0)
    a_turtle.down()
    a_turtle.forward(sides * 0.2)
    
    a_turtle.up()  # The second part of this function will draw hashes for the right window. 
    a_turtle.goto((x + sides * 0.7), (y - sides * 0.2))
    a_turtle.setheading(270.0)
    a_turtle.down()
    a_turtle.forward(sides * 0.2)
    a_turtle.up()
    a_turtle.goto((x + sides * 0.6), (y - sides * 0.3))
    a_turtle.setheading(0.0)
    a_turtle.down()
    a_turtle.forward(sides * 0.2)


def door(a_turtle: Turtle, x: float, y: float, sides: float, R: int, G: int, B: int) -> None:
    """This function draws the door."""
    a_turtle.pencolor("black")
    a_turtle.pensize(2)
    a_turtle.setheading(270.0)
    a_turtle.up()
    a_turtle.goto((x + sides * 0.38), (y - sides))
    a_turtle.down()
    i: int = 0
    a_turtle.fillcolor(R, G, B)
    a_turtle.begin_fill()
    while i < 2:
        a_turtle.left(90)
        a_turtle.forward(sides * .24)
        a_turtle.left(90)
        a_turtle.forward(sides * 0.4)  # For lines 97, 104, and 106: I chose these dimensions because I thought they looked good. Could defnitely play around with them. 
        i += 1
    a_turtle.end_fill()


def doorknob(a_turtle: Turtle, x: float, y: float, sides: float, R: int, G: int, B: int) -> None:
    """This function draws the doorknob."""
    a_turtle.up() 
    a_turtle.goto((x + 0.42 * sides), (y - .8 * sides))  # These are just dimensions I found to be aesthetically pleasing for the doorknob.
    a_turtle.down()
    a_turtle.fillcolor(R, G, B)
    a_turtle.begin_fill()
    a_turtle.circle(3)
    a_turtle.end_fill()
    a_turtle.ht()
    done()


if __name__ == "__main__":
    main()