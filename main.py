# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:51:39 2019

@author: Tsai Jessica
"""

import pygame, random

# Vocabulary 物件
class Vocabulary():
    
    def __init__(self, i):
        self.img = i  # 單字表圖片路徑
        self.voclist = []
    
    def addVocab(self, v):
        self.voclist.append(v)


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
def createMap(word, score, textobj, textrect, wrong):
    screen.fill((232, 232, 232))     # 填充顏色
    if word.vocrect.top < 0 or word.vocrect.bottom > 650:
        speed[1] = -speed[1]
    if word.vocrect.left < 0 or word.vocrect.right > 1100:
        speed[0] = -speed[0]
    screen.blit(word.vocobj, word.vocrect)  

    # 顯示分數
    text = 'Score:' + str(score)
    score_show = font.render(text, True, (255, 255, 255))
    screen.blit(score_show, (100, 50))  # 設定顏色及座標位置
    
    # 顯示錯誤數
    wrongtext = 'Wrong:' + str(wrong)
    wrong_show = font.render(wrongtext, True, (255, 255, 255))
    screen.blit(wrong_show, (100, 150))  # 設定顏色及座標位置
    
    # 顯示打進來的字
    screen.blit(textobj, textrect)
    pygame.display.update()    # 更新顯示

def get_result(score):
    final_text1 = "Game Over"
    final_text2 = "Your final score is: " + str(score)
    ft1_font = pygame.font.SysFont("OpenSans-Regular", 70) #字型和大小
    ft1_surf = ft1_font.render(final_text1, True, (0,0,255)) #顯示的東西,去鋸齒,藍色
    ft2_font = pygame.font.SysFont("OpenSans-Regular", 50)
    ft2_surf = ft2_font.render(final_text2, True, (0,0,255)) #藍色
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100]) # x 讓它置中顯示, y 預設100
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200]) # y 預設200
    pygame.display.flip() # 更新修改的部分

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
    speed = [5,5]  # 移動速度
    condition = 1  # 第幾個畫面
    text = ""  # 輸入的單字
    
    r = random.randint(1, 15)
    img = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\voc\\" + str(r) + ".png"
    voc = Vocabulary(img)
    #background = pygame.image.load("assets/background.png")  # 載入背景圖片
    
    # 讀單字檔並輸入單字列表
    fn = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\voc\\voc" + str(r) + ".csv"
    file = open(fn, 'r', encoding='utf-8')
    for j in file:
        temp = j.split(',')
        voc.addVocab(vocabUnit(temp[0], temp[2]))
    file.close()
    
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
                    screen.blit(background, (0, 0))  # 填入到背景
                    pygame.display.update()
                    i = 0
                elif event.key == pygame.K_RETURN:  # 按下 Enter 鍵
                    if wrong < 4:
                        if i < 9:
                            if text == voc.voclist[i].english:
                                i += 1
                                score += 1
                            else:
                                wrong += 1
                                i += 1
                        else:
                            if text == voc.voclist[i].english:
                                score += 1
                                condition = 3  # 跳到第三個畫面
                            else:
                                condition = 3
                        
                    elif wrong == 4:
                        if i < 9:
                            if text == voc.voclist[i].english:
                                score += 1
                                i += 1
                            else:
                                condition = 3
                        else:
                            if text == voc.voclist[i].english:
                                score += 1
                                condition = 3  # 跳到第三個畫面
                            else:
                                condition = 3
                            
                    text = ""

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode
                    
        textobj = font.render(text, True, (0,0,255))
        textrect = textobj.get_rect(centerx = 150, centery=325)
        
        if condition == 1:
            show_vocabulary(voc.img)  # 顯示單字表畫面
        elif condition == 2:
            createMap(voc.voclist[i], score, textobj, textrect, wrong)
            voc.voclist[i].vocrect = voc.voclist[i].vocrect.move(speed)
        elif condition == 3:
            get_result(score)
        
    pygame.quit()