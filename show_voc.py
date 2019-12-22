# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:17:34 2019

@author: Tsai Jessica
"""

import pygame

def show_vocabulary(path):
    screen.fill((232,232,232))
    picture = pygame.image.load(path)
    screen.blit(picture, (225,0))
    pygame.display.update()

pygame.init()                            # 初始化pygame
pygame.font.init()                       # 初始化字型
font = pygame.font.SysFont("OpenSans-Regular", 40)  # 設定字型和大小
size = width, height = 1100, 650          # 設定視窗
screen = pygame.display.set_mode(size)   # 顯示視窗
img = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\voc\\1.png"
show_vocabulary(img)