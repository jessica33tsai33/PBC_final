# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:45:33 2019

@author: Tsai Jessica
"""

def createMap(word, score):
    screen.fill((232, 232, 232))     # 填充顏色
    #screen.blit(background, (0, 0))  # 填入到背景
    if word.vocrect.top < 0 or word.vocrect.bottom > 650:
        speed[1] = -speed[1]
    screen.blit(word.vocobj, word.vocrect)  # voc指單字本身，voc_pic指承載單字的底圖方塊

    # 顯示分數
    text = 'Score:' + str(score)
    score_show = font.render(text, True, (255, 255, 255))
    screen.blit(score_show, (100, 50))  # 設定顏色及座標位置
    pygame.display.update()    # 更新顯示