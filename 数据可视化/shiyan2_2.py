import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
fig1 = plt.figure(figsize=(20, 25), dpi=90)
# 2018湖北省五个行业年平均
ax1 = fig1.add_subplot(3, 1, 1)
plt.title('2018湖北省五个行业年平均', fontdict=None, loc="center", pad=None)
y = ['农、林、牧、渔业', '采矿业', '制造业', '电力、热力、燃气及水生产和供应业', '建筑业']
x1 = np.array([34280, 51899, 51030, 89643, 53746])
plt.barh(y, x1, height=0.5)
plt.xlabel('收入/元')
ax2 = fig1.add_subplot(3, 1, 2)
# 2019湖北省五个行业年平均
plt.title('2019湖北省五个行业年平均', fontdict=None, loc="center", pad=None)
x2 = np.array([35859, 56938, 54338, 91077, 57477])
plt.barh(y, x2, height=0.5)
plt.xlabel('收入/元')
# 堆积条形图
ax3 = fig1.add_subplot(3, 1, 3)
plt.title('堆积条形图', fontdict=None, loc="center", pad=None)
plt.barh(y, x1, height=0.5)
plt.barh(y, x2, left=x1, height=0.5)
plt.xlabel('收入/元')

plt.show()
