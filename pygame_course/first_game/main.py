import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()
fox_image = pygame.image.load("fox.png")
fox_image = pygame.transform.scale(fox_image, (256,256))
fox_rect = fox_image.get_rect()
fox_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fox_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        fox_rect.x += 5
    screen.fill((205, 0,100)) 
    screen.blit(fox_image, fox_rect)       
    pygame.display.update()
    clock.tick(FPS)