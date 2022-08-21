# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 23:22
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 15连表查询.py
# @Software: PyCharm
import pandas as pd

students = pd.read_excel("source/15Student_Score.xlsx", sheet_name="Students",index_col="ID")
scores = pd.read_excel("source/15Student_Score.xlsx", sheet_name="Scores",index_col="ID")

# 联表查询
# table = students.merge(scores, how="left", on="ID").fillna(0)
# table = students.merge(scores, how="left",left_on=students.index,right_on=scores.index).fillna(0)
# 可以不写 on= "ID"
table = students.join(scores, how="left").fillna(0)
table['Score'] = table['Score'].astype(int)
print(table)
