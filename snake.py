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
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)
def go_up():
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_left():
    snake_head.direction = "left"
def go_right():
    snake_head.direction = "right"
snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_food_pos()
screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

score = 0
scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()


all_tails = []
running = True
while running == True:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}", font=("arial",22), align="center")
    screen.update()
    if snake_head.distance(snake_food) < 20:
        change_food_pos()
        score += 1
        new_tail = create_turtle("square","darkgreen")
        all_tails.append(new_tail)
    move()
    time.sleep(0.2)