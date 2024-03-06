import turtle
import random
import time
import os
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
    if snake_head.direction != "down":
        snake_head.direction = "up"
def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
def go_right():
    if snake_head.direction != "left":
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
if os.path.exists("score.txt"):
    my_file = open("score.txt", "r")
    highscore = int(my_file.read())
else:
    highscore = 0
scoreboard = create_turtle("square", "white")
scoreboard.goto(0, 260)
scoreboard.ht()

def close_my_window():
    global running
    running = False
    my_file = open("score.txt", "w")
    my_file.write(str(highscore))
    my_file.close()


root = screen._root
root.protocol("WM_DELETE_WINDOW", close_my_window)
root.resizable(False, False)

all_tails = []
running = True
while running == True:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}, HighScore:{highscore}", font=("arial",22), align="center")
    screen.update()
    if snake_head.distance(snake_food) < 20:
        change_food_pos()
        score += 1
        if score > highscore:
            highscore = score
        new_tail = create_turtle("square","darkgreen")
        all_tails.append(new_tail)
    
    for i in range(len(all_tails)-1, 0, -1):
        x = all_tails[i-1].xcor()
        y = all_tails[i-1].ycor()
        all_tails[i].goto(x,y)
    if len(all_tails) > 0:
        all_tails[0].goto(snake_head.xcor(), snake_head.ycor())
    
    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(-1  *  snake_head.xcor())
    if snake_head.ycor() > 240:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(240)
        
    move()
    for tail in all_tails:
        if tail.distance(snake_head) < 20:
            snake_head.goto(0,0)
            snake_head.direction = ""
            for tail in all_tails:
                tail.hideturtle()
            score = 0
            all_tails = []
            break
    
        
    time.sleep(0.2)