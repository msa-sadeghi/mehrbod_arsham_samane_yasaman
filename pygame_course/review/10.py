# import turtle

# sc = turtle.Screen()
# sc.bgcolor("orange")
# sc.title("hello")
# sc.setup(700, 600)
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("red")
# t.pencolor("green")
# t.pensize(5)
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# t.shapesize(4)
# turtle.done()



def my_function():
    s = 0
    for i in range(10):
        s += int(input("enter a number: "))
    return s

print(my_function())