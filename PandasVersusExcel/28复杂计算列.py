# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 16:32
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 28复杂计算列.py
# @Software: PyCharm
import numpy as np
import pandas as pd


def get_circumcircle_area(length, height):
    # 求得半径
    r = (np.sqrt(length ** 2 + height ** 2)) / 2
    # 求得圆的面积
    c = r ** 2 * np.pi
    return c


def wrapper(row):
    return get_circumcircle_area(row.Length, row.Height)


rectangles = pd.read_excel("source/28Rectangles.xlsx", index_col="ID")
# axis 扫描的时候是一行一行扫描,
# rectangles['CA'] = rectangles.apply(wrapper, axis=1)
rectangles['CA'] = rectangles.apply(lambda row: get_circumcircle_area(row.Length, row.Height), axis=1)
print(rectangles)
