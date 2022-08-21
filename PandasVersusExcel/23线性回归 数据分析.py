# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 21:52
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 23线性回归 数据分析.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import pandas as pd
# 科学计算范畴的库
from scipy.stats import linregress

sales = pd.read_excel("source/23Sales.xlsx", dtype={"Month": str})

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)

exp = sales.index * slope + intercept

# x轴 是sales.index y轴是sales.Revenue
# plt.bar(sales.index, sales.Revenue)
print(slope * 35 + intercept)

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color="orange")

plt.title(f"y={slope}*x+{intercept}")
# 重新铺了一遍x轴
plt.xticks(sales.index, sales.Month, rotation=90)
# 紧凑布局
plt.tight_layout()
plt.show()
