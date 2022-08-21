# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 15:36
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 26列操作.py
# @Software: PyCharm
import numpy as np
import pandas as pd

page_001 = pd.read_excel("source/26Students.xlsx", sheet_name="Page_001")
page_002 = pd.read_excel("source/26Students.xlsx", sheet_name="Page_002")

# 行插入
# students = pd.concat([page_001, page_002]).reset_index(drop=True)

# 列操作 只需要x轴 改成1 从左到右（很少见）
# students = pd.concat([page_001, page_002],axis=1)


# 追加列
students = pd.concat([page_001, page_002]).reset_index(drop=True)
# students['Age'] = np.repeat(25, len(students))
students['Age'] = np.arange(0, len(students))

# 删除列
students.drop(columns=['Age', 'Score'], inplace=True)

# 插入列
students.insert(1, column="Foo", value=np.repeat("foo", len(students)))

# 修改列名
students.rename(columns={
    "Foo": "FOO",
    "Name": "NAME",

}, inplace=True)

# 去掉所有的空值操作 某些ID是空置

students.ID = students.ID.astype(float)
for i in range(5, 14):
    # 把 5-14 置空
    students.ID.at[i] = np.nan

# 直接删除带有NA的全部删除了
students.dropna(inplace=True)

print(students)
