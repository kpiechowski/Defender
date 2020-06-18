import pygame


class Menu:
    def __init__(self):
        self.bg = pygame.image.load("img/menu.png")
        self.bg = pygame.transform.scale(self.bg, (1100, 700))

        self.start_button = pygame.image.load("img/button.png")
        self.start_button = pygame.transform.scale(self.start_button, (200, 70))
        self.start_pos = 450, 530
        self.start_rect = self.start_button.get_rect(topleft=self.start_pos)

        self.music = pygame.mixer.music.load("lobby.mp3")
        pygame.mixer.music.set_volume(0.2)




    def draw(self, window):
        window.blit(self.bg, (0,0))
        window.blit(self.start_button, self.start_pos)

