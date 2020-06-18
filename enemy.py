import pygame
import random


class Enemy:

    def __init__(self):
        self.health = 100
        self.attack_power = 20
        self.attack_delay = 0
        self.width = 100
        self.height = 100
        self.gold = 100
        self.imgs = [
            pygame.image.load("img/ogr_walk1.png"),
            pygame.image.load("img/ogr_walk2.png"),
            pygame.image.load("img/ogr_walk3.png"),
            pygame.image.load("img/ogr_walk4.png")
        ]
        self.imgs = [pygame.transform.scale(img, (self.width, self.height)) for img in self.imgs]

        self.attak_imgs = [
            pygame.image.load("img/ogr_atack1.png"),
            pygame.image.load("img/ogr_atack2.png")

        ]
        self.attak_imgs = [pygame.transform.scale(img, (self.width, self.height)) for img in self.attak_imgs]

        self.dead_img = pygame.image.load("img/ogr_dead.png")
        self.dead_img = pygame.transform.scale(self.dead_img, (self.width, self.height))
        self.damage = 20
        self.pos_x = random.randint(100, 1000)
        self.pos_y = -300
        self.speed = random.randint(800, 1200)
        self.positions = [(99, 634), (179, 633), (262, 635), (356, 637), (487, 618), (555, 621), (641, 625), (703, 633),
                          (763, 633), (848, 633), (924, 638), (1012, 636)]
        self.animation_count = 0
        self.attak_count = 0
        self.timer = 0
        self.destination = self.positions[random.randint(0, len(self.positions) - 1)]
        self.death_timer = 300

        self.wektor_x = self.destination[0] - self.pos_x
        self.wektor_y = self.destination[1] - self.pos_y

    def attack(self, window):

        self.attack_delay += 1
        window.blit(self.attak_imgs[self.attak_count], (self.pos_x, self.pos_y))
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y - 20, self.health, 10))
        if self.attack_delay % 50 == 0:
            if self.attak_count == 0:
                self.attak_count = 1
                return True
            else:
                self.attak_count = 0
                return False

    def draw(self, window):

        self.timer += 1
        # moving enemies / checking if wall has been reached

        if self.pos_y >= 520:

            return False
        else:
            window.blit(self.imgs[self.animation_count], (self.pos_x, self.pos_y))
            pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y - 20, self.health, 10))
            if self.timer % 25 == 0:
                self.animation_count += 1
                if self.animation_count == len(self.imgs):
                    self.animation_count = 0

            self.pos_y += self.wektor_y / self.speed
            self.pos_x += self.wektor_x / self.speed

    def dead(self, window, x, y):
        if self.death_timer <= 0:
            return True
        # window.blit(self.dead_img, (x, y))
        # self.dead_img.set_alpha(self.death_timer)
        self.blit_alpha(window, self.dead_img, (x, y), self.death_timer)
        self.death_timer -= 5

    def blit_alpha(self,window, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(window, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        window.blit(temp, location)



class Ork(Enemy):

    def __init__(self):
        super().__init__()
