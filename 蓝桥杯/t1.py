import pandas as pd
import numpy as np

zzy = pd.read_excel(r'D:\qq\wd\2630639540\FileRecv\zzy.xlsx')
# print(zzy)
zzy1 = zzy.iloc[2:]
zzy1.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zzy1[8] = [1] * 214
# 转出
zzy2 = zzy1[[3, 4, 8]]
zzy2[3] = zzy2[3].astype("string")
zzy2[4] = zzy2[4].astype("string")
zzy3 = zzy2.groupby([3, 4]).agg({8: 'sum'})
# print(zzy3)
# print("___________________________")
# 转入
zzy4 = zzy1[[5, 6, 8]]
zzy4[5] = zzy4[5].astype("string")
zzy4[6] = zzy4[6].astype("string")
zzy5 = zzy4.groupby([5, 6]).agg({8: 'sum'})
# print(zzy5)
# print("******************")
zzy6 = pd.concat([zzy3, zzy5], axis=1)
zzy6.columns = ['转出', '转入']
zzy6 = zzy6.fillna(0)
zzy6 = zzy6.astype("int64")
print(zzy6)


# 保存成excel文件
zzy6.to_excel(r"D:\1234.xlsx")