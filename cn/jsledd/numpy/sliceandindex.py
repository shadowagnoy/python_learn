import numpy as np

a1 = np.arange(10)
s1 = slice(2, 7, 2)
print(a1[s1])
print(a1[2:7:2])  # 切片参数（start:stop:step）
print(a1[3])  # 对单个元素进行切片
print(a1[3:])  # 对始于索引的元素进行切片
print(a1[3:6])  # 对索引之间的元素进行切片,默认step 1
a2 = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6], [6, 7, 8], [9, 10, 11]])
print(a2[1:])
print(a2[..., 1])  # 返回索引列的ndarray
print(a2[1, ...])  # 返回索引行的ndarray
print(a2[1:, ...])  # 返回第二行之后的行的所有列
print(a2[[0, 1, 2], [0, 1, 0]])  # 该结果包括数组中(0,0)，(1,1)和(2,0)位置处的元素
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
print(a2[rows, cols])  # 包含每个角元素的ndarray对象
print(a2[1:4, [1, 2]])  # 组合使用
print(a2[a2 > 6])  # 切出大于6的元素
a3 = np.array([np.nan, 1, 2, np.nan, 3, 4, 5, 2 + 6j])
print(a3[~np.isnan(a3)])  # 使用了~（取补运算符）来过滤NaN
print(a3[np.iscomplex(a3)])  # 滤掉非复数元素
