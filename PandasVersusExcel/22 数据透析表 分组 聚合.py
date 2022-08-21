# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 17:56
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 22 数据透析表 分组 聚合.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# 显示不全所作的操作
pd.options.display.max_columns = 999

orders = pd.read_excel("source/22Orders.xlsx")
# print(orders.Date.dtype) # datetime64[ns]

orders['Year'] = pd.DatetimeIndex(orders['Date']).year

"""
# 数据透析表 第一种方式
pt1 = orders.pivot_table(index="Category", columns="Year", values="Total",aggfunc=np.sum)
print(pt1)
"""

# 数据透析表 第二种方式 DataFrame手动画图
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame(
    {
        "Sum": s,
        "Count": c
    }
)

print(pt2)
