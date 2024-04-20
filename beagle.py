#!/bin/env python3

import pygame

pygame.init()

GREEN = (100, 255, 80);

screen = pygame.display.set_mode((640, 240))
screen.fill(GREEN)
pygame.display.update()

while True:
    for event in pygame.event.get():
        print(event)
        if (event.type == pygame.QUIT or
            event.type == pygame.KEYDOWN and
            event.key == pygame.K_ESCAPE):

            pygame.quit()
            exit()

