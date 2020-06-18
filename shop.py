import pygame


class Shop:

    def __init__(self):
        self.frame = pygame.image.load("img/shop_frame.png")
        self.frame = pygame.transform.scale(self.frame, (220, 350))

        # dmg up
        self.dmg_img = pygame.image.load("img/button_atac.png")
        self.dmg_img = pygame.transform.scale(self.dmg_img, (40, 40))
        self.dmg_pos = 900, 355
        self.dmg_rect = self.dmg_img.get_rect(topleft=self.dmg_pos)

        self.dmg_upgrade_level = 1
        self.dmg_upgrade_cost = 100
        self.dmg_up = 10

        # speed up
        self.spd_img = pygame.image.load("img/button_speed.png")
        self.spd_img = pygame.transform.scale(self.spd_img, (40, 40))
        self.spd_pos = 900, 409
        self.spd_rect = self.spd_img.get_rect(topleft=self.spd_pos)

        self.spd_upgrade_level = 1
        self.spd_upgrade_cost = 100
        self.spd_up = -2

        # defence up
        self.def_img = pygame.image.load("img/button_def.png")
        self.def_img = pygame.transform.scale(self.def_img, (40, 40))
        self.def_pos = 900, 464
        self.def_rect = self.def_img.get_rect(topleft=self.def_pos)

        self.def_upgrade_level = 1
        self.def_upgrade_cost = 200
        self.def_up = 2

    def draw(self, window):
        window.blit(self.frame, (880, 250))
        window.blit(self.dmg_img, (self.dmg_pos))
        window.blit(self.spd_img, (self.spd_pos))
        window.blit(self.def_img, (self.def_pos))

    def damage_up(self, gold, dmg):
        if gold >= self.dmg_upgrade_cost:
            gold -= self.dmg_upgrade_cost
            dmg += self.dmg_up
            self.dmg_upgrade_level += 1
            self.dmg_upgrade_cost += self.dmg_upgrade_cost
            return gold, dmg
        else:
            return gold, dmg

    def speed_up(self, gold, delay):
        if gold >= self.spd_upgrade_cost:
            gold -= self.spd_upgrade_cost
            delay += self.spd_up
            self.spd_upgrade_level += 1
            self.spd_upgrade_cost += self.spd_upgrade_cost
            return gold, delay
        else:
            return gold, delay

    def defense_up(self, gold, defense):
        if gold >= self.def_upgrade_cost:
            gold -= self.def_upgrade_cost
            defense += self.def_up
            self.def_upgrade_level += 1
            self.def_upgrade_cost *= self.def_upgrade_level
            return gold, defense
        else:
            return gold, defense

# class DamageUp:
#     def __init__(self):
#         # dmg up
#         self.img = pygame.image.load("dmg_up.png")
#         self.img = pygame.transform.scale(self.img, (40, 40))
#         self.pos = 920, 370
#         self.rect = self.img.get_rect(topleft=self.pos)
#
#         self.upgrade_level = 1
#         self.upgrade_cost = 100
#         self.up = 10
#
#     def stat_up(self, gold, stat):
#         if gold >= self.upgrade_cost:
#             gold -= self.upgrade_cost
#             stat += self.up
#             self.upgrade_level += 1
#             self.upgrade_cost *= self.upgrade_level
#             return gold, stat
#         else:
#             return gold, stat