import turtle

my_screen = turtle.Screen()
my_screen.bgcolor('cyan')
my_screen.setup(960, 720)
# my_screen.bgpic("stage1.png")


my_turtle = turtle.Turtle()
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
my_turtle.shape('turtle')
my_turtle.shapesize(2)
my_turtle.color("red")
my_turtle.pensize(4)

for i in range(3):
    my_turtle.forward(120)
    my_turtle.left(120)

for i in range(4):
    my_turtle.forward(120)
    my_turtle.left(90)
for i in range(5):
    my_turtle.forward(120)
    my_turtle.left(360/5)
# TODO

"""
کشیدن مربع سبز
کشیدن هشت ضلعی رنگ قرمز

"""

turtle.done()
