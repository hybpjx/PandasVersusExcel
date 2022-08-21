# _*_ coding: utf-8 _*_
# Time:     2022/7/3 22:33
# Author:   Chen ziChLiang
# Version:  V python3.9
# File:     08filter.py
import pandas as pd


def age_to_18_to_30(age):
    return 18 <= age <= 30


def level_filter(score):
    return 85 <= score <= 100


df = pd.read_excel("source/07filter.xlsx", index_col="ID")
# student = df.loc[df['Age'].apply(age_to_18_to_30)].loc[df['Score'].apply(level_filter)]
# student = df.loc[df.Age.apply(age_to_18_to_30)].loc[df.Score.apply(level_filter)]
# print(student)

# 用lambada 表达式


student = df.loc[df.Age.apply(lambda age: 18 <= age <= 30)].loc[df.Score.apply(lambda score: 85 <= score <= 100)]
print(student)
