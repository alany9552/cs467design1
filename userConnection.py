#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:43:00 2021

@author: huangchengmin
"""

import mailbox
import csv
import pandas as pd
import collections


def removeTime(ss):
    temp = ss.split(' ')
    temp2 = []
    str = ""
    temp2.append(temp[-1])
    # print(temp)
    # for i in (temp):
    #         temp2.append(i[1])

    for i in temp2:
        str = str + i
        str = str + ''

    return str



df = pd.read_csv("dataquery.csv",dtype=str)
fdf=df[df["text"].str.contains("@")]

temp = []
for i in fdf["name"]:
    temp.append(removeTime(i))

t = '"'
print(t)
allNames = []
for i in df["name"]:
    if removeTime(i) not in allNames:
        allNames.append(removeTime(i))


print(allNames)
print((allNames[6]))
s= t+allNames[6]+t
print(s)

ndf=df[df["text"].str.contains(str("EAWAQAA"), na=False)]
print(ndf)
