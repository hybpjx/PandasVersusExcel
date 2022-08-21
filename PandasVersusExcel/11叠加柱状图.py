# -*- coding: utf-8 -*-
# @Time    : 2022/8/9 7:12
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 11叠加柱状图.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel("source/11.xlsx")
# 排序
users["Total"] = users["Oct"] + users["Nov"] + users["Dec"]
users.sort_values(by="Total", inplace=True, ascending=False)

print(users)

# users.plot.bar(x="Name", y=["Oct", "Nov", "Dec"], stacked=True, title="Users") # 纵向的
users.plot.barh(x="Name", y=["Oct", "Nov", "Dec"], stacked=True, title="Users")  # 横向的
plt.tight_layout()
plt.show()
