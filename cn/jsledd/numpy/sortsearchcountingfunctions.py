import numpy as np

a = np.array([[3, 7], [9, 1]])
print(np.sort(a))
print(np.sort(a, axis=0))
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print(np.sort(a, order='age'))

x = np.array([3, 1, 2])
print(x[np.argsort(x)])  # numpy.argsort()函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
# 函数使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。 注意，最后一个键恰好是 sort 的主键
print([nm[i] + ", " + dv[i] for i in ind])
a = np.array([[30, 17, 70], [80, 0, 10], [50, 90, 60]])
'''
numpy.argmax() 和 numpy.argmin()
这两个函数分别沿给定轴返回最大和最小元素的索引。
'''
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.nonzero(a))  # 函数返回输入数组中非零元素的索引
print(a[np.where(a > 40)])  # where()函数返回输入数组中满足给定条件的元素的索引
print(np.extract(np.mod(a, 2) == 0, a))  # where()函数返回输入数组中满足给定条件的元素的索引
print(a.flatten())
