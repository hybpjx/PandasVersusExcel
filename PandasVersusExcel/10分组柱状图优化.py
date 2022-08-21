import pandas as pd
from matplotlib import pyplot as plt

students = pd.read_excel("source/10.xlsx")

# inplace=True 不会生成新的dataframe
# ascending=False 从大到小排
students.sort_values(by=2017, inplace=True, ascending=False)

print(students)

# 分别展示 2016 和2017 颜色分别为橙色和红色
students.plot.bar(x='Field', y=[2016, 2017], color=['orange', 'red'])

# 在这里设置标题为16号字体 粗体
plt.title("Internation Students By Field", fontsize=16, fontweight='bold')

# 设置 x轴y轴名称
plt.xlabel("Field")
plt.ylabel("Number")

# 优化ax轴
ax = plt.gca()
# 第一个参数是操纵对应的 x轴
# rotation="45" 旋转45°
# ha="right" 水平左对齐
ax.set_xticklabels(students["Field"], rotation=45, ha="right")

# 拿到当前的图形
f = plt.gcf()
# 给左面留多大的空间  给底部留多大的空间
f.subplots_adjust(left=0.2, bottom=0.42)


# 这样所有的名字就显示出来了
# plt.tight_layout()

# 展示
plt.show()
