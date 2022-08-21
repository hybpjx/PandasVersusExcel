# _*_ coding: utf-8 _*_
# Time:     2022/7/25 7:15
# Author:   Chen ziChLiang
# Version:  V python3.9
# File:     09.py
import pandas as pd
import numpy
from matplotlib import pyplot as plt
stu = pd.read_excel("source/09.xlsx")
#  光这么写没有用  还需要加上 默认从小到大  ascending = False 是倒序 从大到小
stu.sort_values(by="Number",inplace=True, ascending=False)
# stu.plot.bar(x="Field",y="Number",color="orange",title="International Student by Field")

plt.bar(stu.Field,stu.Number,color="orange")
#  使得我们的Field一列 垂直90°
plt.xticks(stu.Field,rotation="90")
# 行
plt.xlabel("Field")
# 列
plt.ylabel("Number")
# 标题名
plt.title("International Student by Field",fontsize=16)

plt.tight_layout()
plt.show()