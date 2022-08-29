import time

import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(4):
    add_str = str(x)
    if x < 1:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Horny_Mushroom/", "Horny_Mushroom_" + add_str + ".png")),
        (50, 40)))


class Horny_Mushroom(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Horny_Mushroom"
        self.money = 15
        self.max_health = 10
        self.health = self.max_health
        self.imgs = imgs[:]



