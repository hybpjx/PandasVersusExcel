# _*_ coding: utf-8 _*_
"""
Time:     2022/5/31 22:41
Author:   Chen ziChLiang
Version:  V python3.9
File:     02read.py
"""
import pandas as pd

# header　可以指定ｃｏｌｕｍｎ是第几行，也可以设置为Ｎｏｎｅ　那就是默认值了
people = pd.read_excel("ChinaNatureResource.xlsx",header=0)

# 多少行多少列
print(people.shape) # (2985, 12)

# 获得所有的列字段
print(people.columns)

# # 也可以手动修改ｃｏｌｕｍｎｓ
# print(people.columns['id',"......."])

"""
Index(['_id', '采矿权人', '发证机关)', '公告日期)', '开采方式', '开采主矿种', '矿山名称', '面积(km²)',
       '设计生产规模', '项目类型', '许可证号', '有效期)'],
      dtype='object')
"""

# 默认打印头信息 5 行 也可以指定3行
print(people.head(3))
"""
                        _id  ...                   有效期)
0  62217fd75f2cfe5458b98e89  ...  2022-01-09至2023-07-09
1  62217ff15f2cfe5458b98ea4  ...  2017-05-14至2020-12-21
2  62217ff15f2cfe5458b98ea6  ...  2022-02-17至2025-02-17
3  62217ff15f2cfe5458b98ea8  ...  2022-02-17至2025-02-17
4  62217ff15f2cfe5458b98eaa  ...  2022-02-17至2025-02-17
"""

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# 与上述相反 打印尾行，也可以自定义多少行
print(people.tail())