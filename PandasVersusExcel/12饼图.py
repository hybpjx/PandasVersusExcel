# import numpy as np
#
# d = {
#     "rank": [i for i in range(25)],
#     "From": ["巴拿马", "所罗门群岛", "斯洛伐克", "贝宁", "圣多美和普林西比", "埃及", "中非", "冈比亚", "以色列", "科特迪瓦", "佛得角", "亚美尼亚", "波斯尼亚",
#              "阿尔巴尼亚", "比利时", "马来西亚", "伊拉克", "苏里南", "津巴布韦", "伊朗", "布隆迪", "巴勒斯坦", "秘鲁", "立陶宛", "几内亚比绍"
#              ],
#     "'2016": np.random.rand(25),
#     "'2017": np.random.rand(25),
# }


import pandas as pd
import matplotlib.pyplot as plt

# 如果没有指定Index 则自动生成
# 饼图默认是以Index 为图的标签名的
students = pd.read_excel("source/12Students.xlsx", index_col="From")
print(students)

#  默认 就是 ascending = True, False是倒序
#  counterclock 直接改变True 和 False 就是改变的正序和倒序
students["2017"].plot.pie(fontsize=8,counterclock=True)
plt.title("source of international student", fontdict={
    "size": 16,
}, fontweight="bold")
plt.ylabel("2017", fontdict={
    "size": 12,
}, fontweight="bold")
plt.show()

#  但是虽然图画好了 但是是逆时针转的