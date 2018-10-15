import pandas as pd
import numpy as np

print(pd.Series())  # 创建空的系列 默认Series([], dtype: float64)
data = np.array(['a', 'b', 'c', 'd'])
se1 = pd.Series(data)
print(se1)  # 从ndarray 中创建，默认索引是从0开始的整数
se2 = pd.Series(data=data, index=['A', 'B', 'C', 'D'])
print()  # 传递了索引值
data = {'a': 0., 'b': 1., 'c': 2.}
print(pd.Series(data))  # 从字典中创建一个系列
print(pd.Series(5, index=['A', 'B', 'C', 'D']))  # 数据是标量值，则必须提供索引
print(se1[0])  # 指定位置的元素
print(se1[:2])  # 该索引向前的所有项目被提取
print(se1[-3:])  # 该索引的最后三个元素
print(se2['A'])  # 使用标签值检索A索引
print(se2[['A', 'B']])  # 使用标签值检索A,B索引
