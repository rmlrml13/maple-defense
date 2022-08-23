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
        pygame.image.load(os.path.join("game_assets/Pig/", "Pig_" + add_str + ".png")),
        (50, 40)))


class Pig(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Pig"
        self.money = 20
        self.max_health = 5
        self.health = self.max_health
        self.imgs = imgs[:]



