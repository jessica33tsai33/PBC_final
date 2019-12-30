# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:26:27 2019

@author: Tsai Jessica
"""

# 題目類別
class Question():
    
    def __init__(self, e, f, c):
        self.eng = e  # 單字英文
        self.chin = c  # 中文解釋
        self.filt = f  # 英文頭尾


filename = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\questionlistok.csv"
file = open(filename, 'r', encoding = "utf-8")
    
questionlist = []

for i in file:
    temp = i.split(",")
    question = Question(temp[0], temp[1], temp[2])
    questionlist.append(question)

file.close()