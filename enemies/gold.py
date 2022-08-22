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
        pygame.image.load(os.path.join("game_assets/Meso/", "Meso_" + add_str + ".png")),
        (20, 20)))


class Meso(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Meso"
        self.money = 20
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]



