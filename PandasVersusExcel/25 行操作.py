# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 10:34
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 25 行操作.py
# @Software: PyCharm
import pandas as pd

page_001 = pd.read_excel("source/25Students.xlsx", sheet_name="Page_001")
page_002 = pd.read_excel("source/25Students.xlsx", sheet_name="Page_002")
# print(page_001)
# print(page_002)


# # 拼接两张sheet
students = page_001.append(page_002).reset_index(drop=True)  # 即将废弃的方法
# students = pd.concat([page_001, page_002], ignore_index=True)


# # 追加一行
stu = pd.Series({
    "ID": 41,
    "Name": "zic",
    "Score": 99
}, )
#  会生成一个新的
students = students.append(stu, ignore_index=True)
# students.loc[len(students.index)] = ["41", "zic", 99]


# # update 修改表中已有的值
"""
# 这是修改数据  
students.at[39, "Name"] = "billy"
students.at[39, "Score"] = "20"
"""

# 直接替换
stu = pd.Series({
    "ID": 40,
    "Name": "Blink",
    "Score": 91
}, )
students.iloc[39] = stu

# # 插入一行 # 在20 和21 中间插入一行
stu = pd.Series({
    "ID": 101,
    "Name": "Dani",
    "Score": 90
}, )
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)

##  删除一行 从0 - 9 删除
"""
# students.drop(index=[0, 1, 2], inplace=True)
# students.drop(index=range(0,10),inplace=True)
students.drop(index=students[0:10].index, inplace=True)
"""

# # 删除空置
for i in range(1, 15):
    students["Name"].at[i] = ""

missing = students.loc[students.Name == ""]

students.drop(index=missing.index, inplace=True)
students = students.reset_index(drop=True)
print(students)
