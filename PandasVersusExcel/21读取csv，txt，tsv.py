# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 9:47
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 21读取csv，txt，tsv.py
# @Software: PyCharm
import pandas as pd

# 读取csv
students1 = pd.read_csv("source/21/Students.csv", index_col="ID")
print(students1)

# 读取TSV sep 表示以制表符分割
students2 = pd.read_csv("source/21/Students.tsv", index_col="ID", sep="\t")
print(students2)

# 读取tex
students3 = pd.read_csv("source/21/Students.txt", index_col="ID", sep="|")
print(students3)
