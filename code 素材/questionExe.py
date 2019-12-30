# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:39:16 2019

@author: Tsai Jessica
"""

filename = "C:\\Users\\Tsai Jessica\\NTU\\PBC\\Final\\QuestionList.csv"
file = open(filename, 'r', encoding = "utf-8")

eng = []
chin = []
engFilter = []

for i in file:
    question = i.split(",")
    #print(question)
    #print(question[0])
    #print(question[0][0])
    eng.append(question[0])
    chin.append(question[1])
    temp = question[0][0] + "_"
    blank = False
    for j in range(len(question[0])):
        if question[0][j] == " ":
            temp += " " + question[0][j+1] + "_"
            blank = True
    if blank == False:
        temp = question[0][0] + "_" + question[0][-1]
    #temp = question[0][0] + "_" + question[0][-1]
    engFilter.append(temp)

file.close()

fn2 = "questionlistok.csv"
fh2 = open(fn2, "w", encoding = "utf-8")  # try big5 as encoding

for i in range(len(eng)):
	fh2.write(eng[i] + "," + engFilter[i] + "," + chin[i])
fh2.close()