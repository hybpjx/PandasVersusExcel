# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 21:58
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 20行列转换.py
# @Software: PyCharm
import pandas as pd

# 显示不全所作的操作
pd.options.display.max_columns = 999
# 把月份当成Month
videos = pd.read_excel("source/20Videos.xlsx", index_col='Month')
# 转置
table = videos.transpose()
print(table)
