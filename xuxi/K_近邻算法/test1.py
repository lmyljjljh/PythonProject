from sklearn.neighbors import KNeighborsClassifier

# 构造数据集
x = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# 机器学习——模型训练
# 实例化API
estimator = KNeighborsClassifier(n_neighbors=2)
# 使用fit方法进行训练
estimator.fit(x, y)

# 预测其他值
ret = estimator.predict([[10













                          ]])
print(ret)

