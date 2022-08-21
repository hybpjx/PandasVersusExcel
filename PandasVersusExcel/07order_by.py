# _*_ coding: utf-8 _*_
"""
Time:     2022/6/24 6:55
Author:   Chen ziChLiang
Version:  V python3.9
File:     07order_by.py
"""
import pandas as pd


# index_col 指定那一列为索引
df = pd.read_excel("source/b.xlsx",index_col="ID")
# inplace 是在当前进行排序 而不会形成一个新的Dateframe
# ascending = True 是正向排序 false是反向排序
df.sort_values(by="ListPrice",inplace=True,ascending=False)
# 多重排序 后面是ascending 是列表是基于前面的by里面 进行倒还是正
df.sort_values(by=['Name',"Discount"],inplace=True,ascending=[True,False])

print(df)