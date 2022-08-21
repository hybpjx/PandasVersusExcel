# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 21:54
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 17拆分两列.py
# @Software: PyCharm
import pandas as pd

employees = pd.read_excel("source/17Employees.xlsx")

# expand=True 分割成两列
df = employees['Full Name'].str.split('', expand=True)

employees['First Name'] = df[0]
employees['Last Name'] = df[1]

print(employees)
