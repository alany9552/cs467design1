#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:33:43 2021

@author: huangchengmin
"""

import mailbox
import csv
import pandas as pd
import collections

df = pd.read_csv("dataquery.csv",dtype=str)
d={}
print(df)
for i in df['ID']:
    if i not in d.keys():
        d[i]=0


for i in range(13,29):
    s="2021/2/"+str(i)
    fdf=df[df["time"].str.contains(s)]
    for j in fdf['ID']:
        for k in d.keys():
            if j==k :
                d[k]=d[k]+1
    print(i)
    print(d)
    for i in d.keys():
        d[i]=0
