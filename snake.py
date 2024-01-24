import turtle
import random
import time
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(False)
def create_turtle(tshape, tcolor):
    my_turtle = turtle.Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    return my_turtle
def change_food_pos():
    x = random.randint(-270, 270)
    y = random.randint(-270, 240)
    snake_food.goto(x,y)
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
def go_up():
    snake_head.direction = "up"
snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_food_pos()
screen.listen()
screen.onkeypress(go_up,"Up")
running = True
while running == True:
    screen.update()
    move()
    time.sleep(0.2)