import pygame

class Cat:
    def __init__(self, x,y):
        self.all_images = []
        for i in range(1,3):
            img = pygame.image.load(f"costume{i}.svg")
            self.all_images.append(img)
            
        self.image = self.all_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.image_number = 0
        self.last_update_time = 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_update_time > 200:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
        if self.image_number >= len(self.all_images):
            self.image_number = 0
        self.image = self.all_images[self.image_number]
        
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
            
        self.rect.x += dx
        self.rect.y += dy
            
        