# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 15:01
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 13折现趋势图 叠加区域图.py
# @Software: PyCharm
import pandas as pd
from matplotlib import pyplot as plt

orders = pd.read_excel("source/13Orders.xlsx", index_col="Week")
print(orders)
print(orders.columns)  # Index(['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'], dtype='object')

# 绘制折线区域图
# orders.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', ])

# stacked 可以生成堆积条形图或者堆积柱形图
orders.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Components', ], stacked=True)
# orders.plot(y='Accessories')
plt.title("Sales Weekly Trend", fontsize=16, fontweight="bold")
# 左边的那个轴 不要搞混了
plt.ylabel("Total", fontsize=12, fontweight="bold")
# 将横轴重新铺一遍
plt.xticks(orders.index, fontsize=8)
plt.show()
