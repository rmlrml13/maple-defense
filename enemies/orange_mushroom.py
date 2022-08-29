import pygame
import os
from .enemy import Enemy

imgs = []


for x in range(5):
    add_str = str(x)
    if x < 10:
        add_str = add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/Orange_Mushroom/", "Orange_Mushroom_" + add_str + "_0.png")),
        (48, 48)))


class Orange_Mushroom(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Orange_Mushroom"
        self.money = 10
        self.max_health = 8
        self.health = self.max_health
        self.imgs = imgs[:]


