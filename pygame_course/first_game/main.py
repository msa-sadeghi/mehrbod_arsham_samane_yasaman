import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fox_image = pygame.image.load("fox.png")
fox_rect = fox_image.get_rect()
fox_rect.topleft = (0, SCREEN_HEIGHT - 512)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((205, 0,100)) 
    screen.blit(fox_image, fox_rect)       
    pygame.display.update()