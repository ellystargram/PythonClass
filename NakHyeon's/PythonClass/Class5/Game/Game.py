import os
import random

import pygame

gamerootfolder = os.path.dirname(__file__)
resourcefolder = os.path.join(gamerootfolder, "RSC")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()

clock = pygame.time.Clock()
clock.tick(60)

pygame.display.set_caption("Crazy Driver")

road = pygame.image.load(os.path.join(resourcefolder, "Road.png"))
player_png = pygame.image.load(os.path.join(resourcefolder, "Player.png"))
enemy_png = pygame.image.load(os.path.join(resourcefolder, "Enemy.png"))

screen = pygame.display.set_mode(road.get_size())

h = road.get_width() // 2
v = road.get_height() - (player_png.get_height() // 2)

player = pygame.sprite.Sprite()
player.image = player_png
player.surf = pygame.Surface(player.image.get_size())
player.rect = player.surf.get_rect(center=(h, v))

h1 = enemy_png.get_width() // 2
hr = road.get_width() - (enemy_png.get_width() // 2)
h = random.randrange(h1, hr)
v = 0

enemy = pygame.sprite.Sprite()
enemy.image = enemy_png
enemy.surf = pygame.Surface(enemy.image.get_size())
enemy.rect = enemy.surf.get_rect(center=(h, v))

pygame.display.update()

while True:

    screen.blit(road, (0, 0))

    screen.blit(player.image, player.rect)

    screen.blit(enemy.image, enemy.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
