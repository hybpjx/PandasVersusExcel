# _*_ coding: utf-8 _*_
"""
Time:     2022/6/3 8:40
Author:   Chen ziChLiang
Version:  V python3.9
File:     04serial2.py
"""
import pandas as pd

s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="A")
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name="B")
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name="C")

# 如何将上述 列 加到DataFrame

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df)
"""
   A   B    C
1  1  10  100
2  2  20  200
3  3  30  300
"""

df1 = pd.DataFrame([s1,s2,s3])
print(df1)
"""
     1    2    3
A    1    2    3
B   10   20   30
C  100  200  300
"""

a1 = pd.Series([1, 2, 3], index=[1, 2, 3], name="A")
b2 = pd.Series([10, 20, 30], index=[1, 2, 3], name="B")
c3 = pd.Series([100, 200, 300], index=[2, 3, 4], name="C")
df2 = pd.DataFrame({a1.name: a1, b2.name: b2, c3.name: c3})
print(df2)
"""
     A     B      C
1  1.0  10.0    NaN
2  2.0  20.0  100.0
3  3.0  30.0  200.0
4  NaN   NaN  300.0
"""