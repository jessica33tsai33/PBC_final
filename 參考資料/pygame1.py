# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:47:04 2019

@author: Tsai Jessica
"""

import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 320, 240  # 設定視窗大小
screen = pygame.display.set_mode(size)  # 顯示視窗

while True:  # 死迴圈確保視窗一直顯示
    for event in pygame.event.get():  # 遍歷所有事件
        if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
            sys.exit()

pygame.quit()