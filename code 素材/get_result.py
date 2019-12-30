# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:44:25 2019

@author: Tsai Jessica
"""

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
  