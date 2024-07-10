import pygame
from cat import Cat
from pygame.time import Clock
my_cat = Cat(100, 200)
screen_width = 480
screen_height = 360
white = (255, 255, 255)
FPS = 60
c = Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    screen.fill(white) 
    my_cat.draw(screen)
    my_cat.animation()  
    my_cat.move()     
    pygame.display.update()
    c.tick(FPS)