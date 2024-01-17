import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 600)

def create_turtle(tshape, tcolor):
    my_turtle = turtle.Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    return my_turtle


snake_head = create_turtle("square", "green")
# با کمک تابع ساخته شد غذای مار را ایجاد نمایید
# غذای مار دایره ای و قرمز است
# سپس با استفاده از تابع 
# goto
# عذای مار را به مکان دلخواه در صفحه منتقل نمایید.


running = True
while running == True:
    screen.update()