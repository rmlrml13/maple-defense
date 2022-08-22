import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(5):
    add_str = str(x)
    if x < 10:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Snail/", "Snail_" + add_str + "_0.png")),
        (100, 100)))


class Sword(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "sword"
        self.money = 200
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health




