# _*_ coding: utf-8 _*_
"""
Time:     2022/6/3 13:07
Author:   Chen ziChLiang
Version:  V python3.9
File:     05area In.py
"""
# 数据填充  数据区域读取 填充数字
"""
有一些数据 不会在第一行就出现，可能会跳过几行 那像这种 我们该如何处理这些数据呢？
"""
import pandas as pd
from datetime import date, timedelta

"""
# skiprows 跳过六行，
# usercols="C:F" 是只看 C到F这写列的数据
# index_col 是指  把ID设置成前面的索引
# dtype 设置 各个列的字段类型 但是系统不允许我们转换ID为int 所以我们需要转换为 字符串 str
# books=pd.read_excel("a.xlsx",skiprows=6,usecols="C:F",index_col=None,dtype={"ID":str,})
"""
books = pd.read_excel("a.xlsx", skiprows=5, usecols="C:F", index_col=None, dtype=str)

print(type(books["ID"]))  # <class 'pandas.core.series.Series'>

# 调用 at函数
books["ID"].at[0] = 100  # 设置第1个 id为100


# print(books)
def add_mouth(d, md):
    """
    月份校验时间
    :param d: 当前年份
    :param md: 当前传入的月份
    :return:
    """
    # 传入的月份整除12 就是几年
    yd = md // 12
    # 取余
    m = d.month + md % 12

    if m != 12:
        yd += m // 12
        m = m % 12

    return date(d.year + yd, m, d.day)


# 设置时间
now_date = date(2022, 6, 3)

for i in books.index:  # books.index 就是 20 也就是这个数据一共的长度
    # 因为 i是从 0 开始的
    # books["ID"].at[i] = i + 1
    books.at[i,'id'] = i+1
    # 如果i不被2整除就是No 否则就是yes
    books["Instore"].at[i] = "YES" if i % 2 == 0 else "NO"
    books['Date'].at[i] = add_mouth(now_date, i)
print(books)

# 但是有一些小问题 这些id 都是浮点型的 float的
# books.to_excel("b.xlsx",index=False)
