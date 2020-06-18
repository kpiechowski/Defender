import pygame


class Crossbow:

    def __init__(self):
        self.level = 1
        self.img = pygame.image.load("img/crossbow.png")
        self.img = pygame.transform.scale(self.img, (128,128))
        self.pos_x = 495
        self.pos_y = 580
        self.arrows = []
        self.status = "ready"
        self.delay = 30
        self.damage = 50





    def draw(self, window):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        window.blit(self.img, (mouse_x - 64, self.pos_y))

        for arrow in self.arrows:
            window.blit(arrow.img, (arrow.x, arrow.y))
            arrow.y += -10
            if arrow.y <= -128:
                self.arrows.remove(arrow)

    def shoot(self):

            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.arrows.append(Arrow(mouse_x-12))


class Arrow:

    def __init__(self, x):
        self.img = pygame.image.load("img/arrow.png")
        self.img = pygame.transform.scale(self.img, (30,118))
        self.x = x
        self.y = 600
