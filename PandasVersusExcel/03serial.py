# _*_ coding: utf-8 _*_
# Time:     2022/6/1 23:16
# Author:   Chen ziChLiang
# Version:  V python3.9
# File:     03serial.py
import pandas as pd
# Series 和python中的字典很像
d={
    "x":100,
    "y":200,
    "z":300,
}

# 会把key转换为Index，value转换为data
# 生成序列
s1=pd.Series(d)

print(s1._data)# SingleBlockManager Items: Index(['x', 'y', 'z'], dtype='object') NumericBlock: 3 dtype: int64
print(s1.index) # Index(['x', 'y', 'z'], dtype='object')
print(s1.name) # None