import pygame
from .tower import Tower
import os
import math
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "side.jpg")), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")),
                                     (50, 50))

tower_imgs1 = []
for x in range(7):
    tower_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Character/Warrior_" + str(x) + ".png")),
        (88, 90)))

effect_imgs = []
for x in range(5):
    effect_imgs.append(pygame.transform.scale(
        pygame.image.load((os.path.join("game_assets/Effect/magic_effect_" + str(x) + ".png"))),
        (50, 50)))


class Warrior(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_count = 0
        self.range = 220
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 3
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "warrior"

        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, 2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade1")

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.tower_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.tower_imgs[self.archer_count // 10]
        if self.left == True:
            add = -45
        else:
            add = -archer.get_width() + 10
        win.blit(archer, ((self.x + add), (self.y - archer.get_height() + 45)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt(
                (self.x - enemy.img.get_width() / 2 - x) ** 2 + (self.y - enemy.img.get_height() / 2 - y) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 50:
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not (self.left):
                self.left = True
                for x, img in enumerate(self.tower_imgs):
                    self.tower_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.tower_imgs):
                    self.tower_imgs[x] = pygame.transform.flip(img, True, False)

        return money


tower_imgs2 = []
for x in range(5):
    tower_imgs2.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Effect/magic_effect_" + str(x) + ".png")),
        (60, 90)))


class Archer(Warrior):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs2[:]
        self.archer_count = 0
        self.range = 400
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage

        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, 2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade2")
        self.name = "archer"


tower_imgs3 = []
for x in range(6):
    tower_imgs3.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Orange_Mushroom/Orange_Mushroom_" + str(x) + "_0.png")),
        (60, 90)))


class Bandit(Warrior):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs3[:]
        self.archer_count = 0
        self.range = 300
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage

        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, 2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade3")
        self.name = "bandit"


tower_imgs4 = []
for x in range(6):
    tower_imgs4.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Character/Wizard_" + str(x) + ".png")),
        (80, 90)))


class Wizard(Warrior):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs4[:]
        self.archer_count = 0
        self.range = 350
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage

        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, 2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade4")
        self.name = "wizard"
