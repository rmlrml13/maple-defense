import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(5):
    add_str = str(x)
    if x < 10:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Balrog/", "Balrog_" + add_str + ".png")),
        (120, 110)))


class Balrog(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "Balrog"
        self.money = 1000
        self.imgs = imgs[:]
        self.max_health = 200
        self.health = self.max_health




