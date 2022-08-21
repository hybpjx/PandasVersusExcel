# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 15:35
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : 14散点图，直方图.py
# @Software: PyCharm
# import pandas as pd
# import numpy as np
#
# price_list = []
# for i in range(1, 50):
#     uuid = ''.join(map(str, np.random.randint(0, 9, 3))) + ''.join(map(str, np.random.randint(0, 9, 3)))
#     price_list.append(uuid)
# print(price_list)
# id_list = []
# for i in range(1, 50):
#     uuid = ''.join(map(str, np.random.randint(0, 9, 4))) + ''.join(map(str, np.random.randint(0, 9, 4)))
#     id_list.append(uuid)
# print(id_list)
#
# df = pd.DataFrame(
#     {
#         "id": id_list,
#         "price": price_list
#     }
# )
# df.to_excel("source/14.xlsx",index=False)


import pandas as pd
from matplotlib import pyplot as plt

#  显示所有列
pd.options.display.max_columns = 777
homes = pd.read_excel("source/14.xlsx", )

print(homes.corr())



# # print(homes.head())
#
# # 散点图
# # homes.plot.scatter(y="sqft_living", x="price")
# # plt.show()
#
#
# # # bins = 100 让图表更细腻
# # homes['price'].plot.hist(bins=100)
# # # xticks 重新铺一遍x轴 rotation = 90 让他竖起来
# # plt.xticks(range(0, max(homes['price']), 100), fontsize=12, rotation=90)
# # plt.show()
#
# homes['sqft_living'].plot.kde()
# plt.xticks(range(0, max(homes['sqft_living']), 100), fontsize=12, rotation=90)
# plt.show()