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
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)