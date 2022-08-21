# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 22:11
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 18求和求平均.py
# @Software: PyCharm
import pandas as pd

students = pd.read_excel("source/18Students.xlsx",index_col="ID")

# 拿到三次成绩的子集
temp = students[['Test_1', 'Test_2', 'Test_3']]

# result = temp.sum()
# print(result) # 拿到的是一列的总和  不是某一行的总和

#  axis = 1 指定横轴
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', "Total", "Average"]].mean()
col_mean['Name'] = "Summary"

students = students.append(col_mean, ignore_index=True)

print(students)
