import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'

#matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
#-*- coding=utf-8 -*-
# Build a dataframe with your connections
# plt.rcParams['axes.unicode_minus'] = False ## 设置正常显示符号
colorList = [1, 2, 1, 1, 1, 22, 3, 1, 1, 1, 1, 1 ,1,
4,1,2,6,3,2,2,2,1,2,2,2,22,3,1,1,1,1,1,1]


weightedList = []
for i in colorList:
    if i<10:
        i=i+10
    weightedList.append(i)

df = pd.DataFrame({ 'from':['大魔王', '大魔王', '阿杰','大魔王','拉菲', '拉菲','帝国の炊事员', '.','赤城乳业','SFXZ','没药微焰❀', '阿杰', '暧昧子弟兵', '大魔王', '群空气', '拉菲','大魔王','拉菲','帝国の炊事员','大魔王','赤城乳业','赤城乳业','大魔王','大魔王','大魔王','拉菲','帝国の炊事员','.','赤城乳业','SFXZ','没药微焰❀','阿杰','暧昧子弟兵'],
'to':['小阁', '赤城乳业', '赤城乳业','没药微焰❀','没药微焰❀', '大魔王', '大魔王', '大魔王', '大魔王', '大魔王', '大魔王', '大魔王', '大魔王','拉菲','拉菲','群空气','阿杰','阿杰','阿杰','帝国の炊事员','帝国の炊事员','волк','SFXZ','暧昧子弟兵','testtest','Mimic','Mimic','Mimic','Mimic','Mimic','Mimic','Mimic','Mimic'],
'value':weightedList})


print(weightedList)
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph() )
# Custom the nodes:
pos = nx.circular_layout(G)
# nx.draw(G, with_labels=True, connectionstyle='arc3, rad = 0.1', node_color='skyblue', node_size=1500,arrows=False, edge_color=df['value'], width=10.0, edge_cmap=plt.cm.gray)
nx.draw(G, with_labels=True,connectionstyle='arc3, rad = 0.5',
        node_color='skyblue', node_size=2200,
        edge_color=df['value'], width=3, edge_cmap=plt.cm.YlOrRd,
        arrowstyle='->',arrowsize=20,
        font_size=10, font_weight="bold",
        pos=nx.random_layout(G, seed=13))

plt.show()
