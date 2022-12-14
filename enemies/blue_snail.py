import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(4):
    add_str = str(x)
    if x < 10:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Blue_Snail/", "Blue_Snail_" + add_str + "_0.png")),
        (42, 42)))


class Blue_Snail(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "blue_snail"
        self.money = 5
        self.imgs = imgs[:]
        self.max_health = 4
        self.health = self.max_health



