import random
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
duck_rect.bottomleft = (0, random.randint(96,1000))
# duck_rect.left = 0
# duck_rect.bottom = SCREEN_HEIGHT


f = pygame.font.Font("Abrushow.ttf",32)
score_text = f.render(f"Score:{score}", True, (255, 255, 255))
score_rect = score_text.get_rect()
score_rect.topleft = (0,0)

# pygame.mixer.music.load("Drip Drop.wav")
# pygame.mixer.music.play(-1)
bg_music = pygame.mixer.Sound("Drip Drop.wav")
bg_music.play(-1)

chomp_sound = pygame.mixer.Sound("Chomp.wav")
chomp_sound.set_volume(0.5)
flip = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fox_rect.x -= 5
        flip = False
    if keys[pygame.K_RIGHT]:
        fox_rect.x += 5
        flip = True
    duck_rect.x += 5
    if duck_rect.right >= SCREEN_WIDTH:
        duck_rect.bottomleft = (0, SCREEN_HEIGHT)
    
    if fox_rect.colliderect(duck_rect):
        duck_rect.bottomleft = (0, random.randint(0,1000))
        score += 1
        chomp_sound.play()
        
    score_text = f.render(f"Score:{score}", True, (255, 255, 255))    
    screen.fill((205, 0,100)) 
    screen.blit(pygame.transform.flip(fox_image, flip, False), fox_rect)       
    screen.blit(duck_image, duck_rect)
    screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)