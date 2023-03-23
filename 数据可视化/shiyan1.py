import matplotlib.pyplot as plt
import numpy as np

# matplotlib其实是不支持显示中文的 显示中文需要一行代码设置字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
jsl = [644, 730, 664.8, 682.5, 651.3, 706.5, 691.6]
print(jsl)
fig = plt.figure()
ax = fig.add_subplot(111)
x = ['2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年']

ax.barh(x, jsl, align = 'center', alpha = 0.5)

plt.ylabel('年份')
plt.xlabel('降水量（mm）')

# # 设置数字标签
# for a, b in zip(x, jsl):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
plt.show()
