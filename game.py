import pygame
from crossbow import Crossbow
from enemy import Enemy
from interface import Interface
from shop import Shop
from menu import Menu
import math

pygame.init()


class Game:
    def __init__(self):
        self.menu = Menu()
        self.window_w = 1100
        self.window_h = 700
        self.wave = 0
        self.player_gold = 0
        self.bg = pygame.image.load("img/bg.png")
        self.bg = pygame.transform.scale(self.bg, (self.window_w, self.window_h))
        self.run = True
        self.shop = Shop()
        self.shop_upgrades = [self.shop.dmg_rect, self.shop.def_rect, self.shop.spd_rect]
        self.interface = Interface()
        self.crossbow = Crossbow()
        self.enemies = []
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        self.hp = 1500
        self.defense = 0
        self.game_status = "menu"  # running / shop / menu
        self.wave_button = pygame.image.load("img/button.png")
        self.wave_button = pygame.transform.scale(self.wave_button, (200, 60))
        self.wave_button_pos = 30, 530
        self.wave_button_rect = self.wave_button.get_rect(topleft=self.wave_button_pos)

    def draw(self):

        self.window.blit(self.bg, (0, 0))
        self.crossbow.draw(self.window)
        self.interface.draw(self.window)
        for enemy in self.enemies:

            if enemy.health > 0:
                if enemy.draw(self.window) == False:
                    enemy.attack(self.window)
                    if enemy.attack(self.window) == True:
                        self.hp -= (enemy.attack_power - self.defense)
                else:
                    enemy.draw(self.window)
            else:
                if enemy.dead(self.window, enemy.pos_x, enemy.pos_y) == True:
                    self.enemies.remove(enemy)

        # wave font
        font = pygame.font.Font('freesansbold.ttf', 20)
        wave = font.render("WAVE: " + str(self.wave), True, (255, 255, 255))
        self.window.blit(wave, (1000, 20))

        # castle hp
        pygame.draw.rect(self.window, (255, 0, 0), (25, 20, self.hp / 5, 10))

        # player gold
        gold = font.render(str(self.player_gold), True, (255, 255, 0))
        self.window.blit(gold, (60, 70))


        # wave button
        if self.game_status is "shop":
            self.window.blit(self.wave_button, (self.wave_button_pos))
            self.shop.draw(self.window)

            # shop fonts
            dmg_font = font.render(str(self.shop.dmg_upgrade_cost), True, (255, 255, 0))
            speed_font = font.render(str(self.shop.spd_upgrade_cost), True, (255, 255, 0))
            def_font = font.render(str(self.shop.def_upgrade_cost), True, (255, 255, 0))

            self.window.blit(dmg_font, (950, 367))
            self.window.blit(speed_font, (950, 420))
            self.window.blit(def_font, (950, 476))

        if self.game_status is "menu":
            self.menu.draw(self.window)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)

    def if_hit(self):
        for enemy in self.enemies:
            if enemy.health > 0:
                for arrow in self.crossbow.arrows:
                    dist = math.sqrt(math.pow((arrow.x + 15) - (enemy.pos_x + enemy.width / 2 - 10), 2) + math.pow(
                        arrow.y - (enemy.pos_y + enemy.height / 2), 2))
                    if dist < 50:
                        enemy.health -= self.crossbow.damage
                        self.crossbow.arrows.remove(arrow)
                        if enemy.health <= 0:
                            # d_pos_x = enemy.pos_x
                            # d_pos_y = enemy.pos_y
                            self.player_gold += enemy.gold
                            # enemy.dead()

    def spawn_enemies(self):
        self.wave += 1
        self.enemies = [Enemy() for x in range(0, 3 + self.wave)]

    def death(self):
        pass

    def running(self):
        clock = pygame.time.Clock()

        time = 0
        shot_time = 0
        while self.run:
            clock.tick(60)
            time += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_status is "menu":
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if pygame.Rect.collidepoint(self.menu.start_rect, mouse_x, mouse_y):
                            self.game_status = "shop"
                    if self.game_status is "running":
                        if self.crossbow.status == "ready":
                            self.crossbow.status = "reloading"
                            self.crossbow.shoot()
                    elif self.game_status is "shop":
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if pygame.Rect.collidepoint(self.wave_button_rect, mouse_x, mouse_y):
                            self.game_status = "running"
                            self.spawn_enemies()
                        # shop icon clicked
                        elif pygame.Rect.collidepoint(self.shop.dmg_rect, mouse_x, mouse_y):
                            print(self.crossbow.damage, " ", self.shop.dmg_upgrade_level, " ",
                                  self.shop.dmg_upgrade_cost)
                            self.player_gold, self.crossbow.damage = self.shop.damage_up(self.player_gold,
                                                                                         self.crossbow.damage)

                        elif pygame.Rect.collidepoint(self.shop.spd_rect, mouse_x, mouse_y):
                            self.player_gold, self.crossbow.delay = self.shop.speed_up(self.player_gold,
                                                                                       self.crossbow.delay)
                            print(self.crossbow.delay, " ", self.shop.spd_upgrade_cost)

                        elif pygame.Rect.collidepoint(self.shop.def_rect, mouse_x, mouse_y):
                            self.player_gold, self.defense = self.shop.defense_up(self.player_gold, self.defense)
                            print(self.defense, " ", self.shop.def_upgrade_cost)

            # crossbow shooting
            if shot_time % self.crossbow.delay == 0:
                self.crossbow.status = "ready"
                shot_time = 1

            if self.crossbow.status == "reloading":
                shot_time += 1
            # no enemies on battlefield
            if not self.enemies and self.wave >= 1:
                self.game_status = "shop"

            # if castle hp is equal 0
            if self.hp <= 0:
                self.hp = 0
                self.game_status = "end"
                self.death()

            self.draw()
            self.if_hit()

            pygame.display.update()


game = Game()
game.running()
