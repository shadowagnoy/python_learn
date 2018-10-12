import numpy as np

a = np.arange(6)
b = a
b.shape = 3, 2
print(a)
print(id(a) == id(b))  # 直接使用 =  复制 a和b 完全一致
c = a.view()
print(id(a) == id(c))  # 浅复制 它是一个新的数组对象，并可查看原始数组的相同数据。 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。
c[[0, 0]] = 20
print(a)  # 浅复制 共享同一套数据  创建视图
d = a.copy()
print(id(a) == id(d))
d[[1, 1]] = 30
print(a)  # ndarray.copy()函数创建一个深层副本。 它是数组及其数据的完整副本，不与原始数组共享
s = a[:, :2]  # !!! 切片属于浅复制 创建视图
s[[1, 1]] = 40
print(a)
