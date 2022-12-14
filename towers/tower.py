import pygame
from menu.menu import Menu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "side.jpg")), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")), (50, 50))


class Tower:
    """
    Abstract class for towers
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

        self.tower_imgs = []
        self.damage = 1

        self.place_color = (0, 0, 255, 100)

    def draw(self, win):
        # draw menu
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self, win):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width() // 2 + self.width and X >= self.x - img.get_width() // 2:
            if Y <= self.y + self.height - img.get_height() // 2 and Y >= self.y - img.get_height() // 2:
                return True
        return False

    def sell(self):
        return self.sell_price[self.level - 1]

    def upgrade1(self):
        if self.level == 1:
            self.tower_imgs.clear()
            for x in range(6):
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/Character/Warrior2_" + str(x) + ".png")),
                    (110, 120)))
            self.level += 1
            self.damage += 3
        elif self.level == 2:
            self.tower_imgs.clear()
            for x in range(6):
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/Character/Warrior3_" + str(x) + ".png")),
                    (150, 120)))
            self.level += 1
            self.damage += 3

    def upgrade2(self):
        if self.level < len(self.tower_imgs):
            self.tower_imgs.clear()
            for x in range(6):
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/Character/Warrior2_" + str(x) + ".png")),
                    (110, 120)))
            self.level += 1
            self.damage += 3

    def upgrade3(self):
        if self.level < len(self.tower_imgs):
            self.tower_imgs.clear()
            for x in range(6):
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/Character/Warrior2_" + str(x) + ".png")),
                    (110, 120)))
            self.level += 1
            self.damage += 3

    def upgrade4(self):
        if self.level < len(self.tower_imgs):
            self.tower_imgs.clear()
            for x in range(6):
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/Character/Wizard2_" + str(x) + ".png")),
                    (100, 85)))
            self.level += 1
            self.damage += 2

    def get_upgrade_cost(self):
        return self.price[self.level - 1]

    def move(self, x, y):

        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    # ?????? ?????? ??????
    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dis >= 100:
            return False
        else:
            return True
