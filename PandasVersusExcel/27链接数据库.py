# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 16:24
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 27链接数据库.py
# @Software: PyCharm
import pandas as pd
import pyodbc
import sqlalchemy

connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')
query = 'SELECT FirstName, LastName FROM Person.Person'
df1 = pd.read_sql(query, connection)

df2 = pd.read_sql(query, engine)
print(df1)
print(df2)
