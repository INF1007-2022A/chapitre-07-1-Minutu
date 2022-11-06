import turtle

pegasus = turtle.Turtle()
pegasus.getscreen().bgcolor('#994444')

pegasus.speed(speed=10)
def star(pegasus, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            pegasus.forward(size)
            star(pegasus, size/3)
            pegasus.left(216)
        turtle.end_fill()
star(pegasus, 360)






turtle.done()