import pygame

class Cat:
    def __init__(self, x,y):
        self.right_images = []
        self.left_images = []
        for i in range(1,3):
            img = pygame.image.load(f"costume{i}.svg")
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
            
            
        self.image = self.right_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.image_number = 0
        self.last_update_time = 0
        self.direction = 1
        self.moving = False
        
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        
    def animation(self):
        if self.moving:
            if pygame.time.get_ticks() - self.last_update_time > 200:
                self.last_update_time = pygame.time.get_ticks()
                self.image_number += 1
            if self.image_number >= len(self.right_images):
                self.image_number = 0
        if self.direction == 1:
            self.image = self.right_images[self.image_number]
        elif self.direction == -1:
            self.image = self.left_images[self.image_number]
        
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.flip = True
            self.moving = True
            dx -= 5
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            dx += 5
            self.direction = 1
            self.moving = True
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
            
            
            
            
        self.rect.x += dx
        self.rect.y += dy
            
        