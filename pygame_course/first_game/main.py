import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
score = 0
clock = pygame.time.Clock()
fox_image = pygame.image.load("fox.png")
fox_image = pygame.transform.scale(fox_image, (256,256))
fox_rect = fox_image.get_rect()
fox_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)


duck_image = pygame.image.load("d.png")
duck_image = pygame.transform.scale(duck_image, (96,96))
duck_image = pygame.transform.flip(duck_image, True, False)
duck_rect = duck_image.get_rect()
duck_rect.bottomleft = (0, SCREEN_HEIGHT)
# duck_rect.left = 0
# duck_rect.bottom = SCREEN_HEIGHT

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
    duck_rect.x += 5
    if duck_rect.right >= SCREEN_WIDTH:
        duck_rect.bottomleft = (0, SCREEN_HEIGHT)
    
    if fox_rect.colliderect(duck_rect):
        duck_rect.bottomleft = (0, SCREEN_HEIGHT)
        score += 1
        
        
    screen.fill((205, 0,100)) 
    screen.blit(fox_image, fox_rect)       
    screen.blit(duck_image, duck_rect)       
    pygame.display.update()
    clock.tick(FPS)