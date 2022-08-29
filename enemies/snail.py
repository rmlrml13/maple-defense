import time

import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(5):
    add_str = str(x)
    if x < 1:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Snail/", "Snail_" + add_str + "_0.png")),
        (32, 32)))


class Snail(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Snail"
        self.money = 5
        self.max_health = 2
        self.health = self.max_health
        self.imgs = imgs[:]



