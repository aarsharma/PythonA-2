# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,400))

player=pygame.Rect(200,50,40,40)
playerspeed= -2

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
          

    if player.y == 0:
        playerspeed=6
        

    if player.y == 360:
        playerspeed=playerspeed * -1

    player.y=player.y+playerspeed
    

    pygame.draw.rect(screen,(23,100,100),player)
    


    pygame.display.update()
    clock.tick(30)
