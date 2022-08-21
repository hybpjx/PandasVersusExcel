# -*- coding: utf-8 -*-
# @Time    : 2022/8/18 23:53
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 19定位 删除重复值.py
# @Software: PyCharm
import pandas as pd

students = pd.read_excel("source/19Students_Duplicates.xlsx")
dupe = students.duplicated(subset=["Name"])
print(dupe.any())  # 是否有重复数据

# dupe = dupe[dupe == True]
dupe = dupe[dupe]
print(dupe.index)  # Int64Index([20, 21, 22, 23, 24], dtype='int64')

# 定位重复数据
print(students.iloc[dupe.index])