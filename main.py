# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:51:39 2019

@author: Tsai Jessica
"""

import pygame, random

# Vocabulary 物件
class Vocabulary():
    
    def __init__(self, i):
        #self.english = []  # 單字英文list
        #self.chinese = []  # 單字中文list
        self.img = i  # 單字表圖片路徑
        self.voclist = []
        
    #def read_eng(self, e):  # 讀入英文單字
    #    self.english.append(e)
    
    #def read_chi(self, c):  # 讀入中文單字
    #    self.chinese.append(c)
    
    def addVocab(self, v):
        self.voclist.append(v)
    
    #def check_voc(self, e):
    #    for i in self.voclist:
    #        if i.english == e:
    #            return i


# 單一Vocab物件
class vocabUnit():
    
    def __init__(self, e, c):
        self.english = e
        self.chinese = c
        self.vocobj = font.render(self.chinese, True, (0, 0, 255))
        self.vocrect = self.vocobj.get_rect(centerx = 550)


# 顯示單字表
def show_vocabulary(path):
    screen.fill((232,232,232))  # 設定背景顏色
    picture = pygame.image.load(path)  # 讀入單字表圖片
    screen.blit(picture, (225,0))  # 單字表圖片置中
    pygame.display.update()


# 單字塊下降
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


# 主程式
if __name__ == '__main__':
    
    # 初始畫面設定
    pygame.init()                            # 初始化pygame
    pygame.font.init()                       # 初始化字型
    font = pygame.font.Font("NotoSansCJKtc-Medium.otf", 30)  # 設定字型和大小
    size = width, height = 1100, 650          # 設定視窗
    screen = pygame.display.set_mode(size)   # 顯示視窗
    clock = pygame.time.Clock()              # 設定時鐘
    background = pygame.image.load("bg.png")
    
    # 變數宣告
    score = 0  # 分數
    i = 0  # 單字序號
    wrong = 0  # 錯誤次數
    speed = [0,5]  # 移動速度
    condition = 1
    
    r = random.randint(1, 15)
    img = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\voc\\" + str(r) + ".png"
    voc = Vocabulary(img)
    #background = pygame.image.load("assets/background.png")  # 載入背景圖片
    
    # 讀單字檔並輸入單字列表
    fn = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\voc\\voc" + str(r) + ".csv"
    file = open(fn, 'r', encoding='utf-8')
    for j in file:
        #j = j.encode('utf-8').decode('utf-8-sig')
        temp = j.split(',')
        
        #voc.read_eng(temp[0])
        #voc.read_chi(temp[2])
        voc.addVocab(vocabUnit(temp[0], temp[2]))
    file.close()
    #voc.addVocab(vocabUnit(temp[0], temp[2]))
    
    # 開始遊戲
    running = True
    while running == True:
        clock.tick(60)  # 控制速度
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:  # 按下鍵
                if event.key == pygame.K_SPACE:  # 按下空白鍵
                    condition = 2
                    #creat_map(0, score)  # 第一個單字掉下來
                    screen.blit(background, (0, 0))  # 填入到背景
                    pygame.display.update()
                    i = 0
                #elif event.key == pygame.K_KP_ENTER:  # 按下 Enter 鍵
                #    if wrong < 4:
                #    
                #    elif wrong == 4:
        if condition == 1:
            show_vocabulary(voc.img)  # 顯示單字表畫面
        elif condition == 2:
            createMap(voc.voclist[i], score)
            voc.voclist[i].vocrect = voc.voclist[i].vocrect.move(speed)
        
    #elif event.key == pygame.K_KP_ENTER:  # 按下 Enter 鍵
    pygame.quit()