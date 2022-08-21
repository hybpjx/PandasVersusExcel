# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 9:58
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 24标记颜色.py
# @Software: PyCharm
import pandas as pd


def low_score_red(s):
    color = "red" if s < 60 else "black"
    return f"color:{color}"


def highest_score_green(col):
    return ["background-color:lime" if s == col.max() else "background-color:white" for s in col]


students = pd.read_excel(r"E:\PandasVersusExcel\source\24Students.xlsx")
# 无差别的识别在显示区域
students.style.applymap(low_score_red, subset=["Test_1", "Test_2", "Test_3"]).apply(highest_score_green,
                                                                                    subset=["Test_1", "Test_2",
                                                                                            "Test_3"])
