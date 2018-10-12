import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
'''
numpy.amin() 和 numpy.amax()
这些函数从给定数组中的元素沿指定轴返回最小值和最大值
'''
print(np.amin(a, axis=0))
print(np.ptp(a, axis=1))  # numpy.ptp()函数返回沿轴的值的范围（最大值 - 最小值）
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=1))  # 分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
print(np.median(a, axis=0))  # 中值定义为将数据样本的上半部分与下半部分分开的值
print(np.mean(a, axis=0))  # 算术平均值是沿轴的元素的总和除以元素的数量
a = np.array([1, 2, 3, 4])
print(np.average(a))  # 加权平均值 不指定权重时相当于 mean 函数
wts = np.array([4, 3, 2, 1])
print(np.average(a, weights=wts))
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))  # 如果 returned 参数设为 true，则返回权重的和
a = np.arange(6).reshape(3, 2)
print(a)
wt = np.array([3, 5])
print(np.average(a, axis=1, weights=wt))
print(np.std([1, 2, 3, 4]))  # 标准差是与均值的偏差的平方的平均值的平方根 公式:std = sqrt(mean((x - x.mean())**2))
print(np.var([1, 2, 3, 4]))  # 方差是偏差的平方的平均值，即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根
