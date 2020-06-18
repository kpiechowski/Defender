import pygame

class Interface:

    def __init__(self):
        self.heart = pygame.image.load("img/heart.png")
        self.heart = pygame.transform.scale(self.heart, (30,30))
        self.gold = pygame.image.load("img/gold.png")
        self.gold = pygame.transform.scale(self.gold, (30, 30))


    def draw(self, window):
        window.blit(self.heart , (10, 10))
        window.blit(self.gold , (10, 60))