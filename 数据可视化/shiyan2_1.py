import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
x = ['文科', '理科']
y1 = np.array([11865, 51615])
y2 = np.array([11389, 51271])
# 2018
fig1 = plt.figure(figsize=(10, 10), dpi=90)  # 确定画布大小
ax1 = fig1.add_subplot(1, 3, 1)  # 绘制第1幅子图
plt.title('2018年一本上线人数', fontdict=None, loc="center", pad=None)
plt.bar(x, y1, width=0.3)
# # 设置数字标签
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
plt.ylabel('人数/人')
# 2019
ax2 = fig1.add_subplot(1, 3, 2)  # 绘制第2幅子图
plt.title('2019年一本上线人数', fontdict=None, loc="center", pad=None)
plt.bar(x, y2, width=0.3)
# # 设置数字标签
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
plt.ylabel('人数/人')
# plt.show()
ax3 = fig1.add_subplot(1, 3, 3)  # 绘制第2幅子图
plt.bar(x, y1, width=0.3)
plt.bar(x, y2, bottom=y1, width=0.3)
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
for a, b in zip(x, y1+y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
plt.ylabel('人数/人')
plt.show()
