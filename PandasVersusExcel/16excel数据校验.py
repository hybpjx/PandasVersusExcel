# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 6:50
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 16excel数据校验.py
# @Software: PyCharm
import pandas as pd


# def score_validation(row):
#     try:
#         assert 0 <= row.Score <= 100
#     except:
#         print(f"#{row.ID}\tstudent{row.Name} has an invalid score{row.Score}")
def score_validation(row):
    if not 0 <= row.Score <= 100:
        print(f"#{row.ID}\tstudent{row.Name} has an invalid score{row.Score}")


students = pd.read_excel("source/16Students.xlsx")

students.apply(score_validation, axis=1)

# 数据清理与更正
