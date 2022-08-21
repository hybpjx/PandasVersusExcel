# _*_ coding: utf-8 _*_
"""
Time:     2022/6/17 6:56
Author:   Chen ziChLiang
Version:  V python3.9
File:     06 computed.py
"""
import pandas as pd

books = pd.read_excel("source/b.xlsx", index_col='ID')
# print(books)
# books['Price'] = books['ListPrice']*books['Discount']

# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
for i in range(5, 16):  # 仅仅计算5,16列的的
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

print(books)

## 每本书涨两块钱 如何计算
# 第一种方式
books['ListPrice'] += 2
print(books)


# 第二种方式 调用apply
def add_2(x):
    return x + 2


books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)
print(books)