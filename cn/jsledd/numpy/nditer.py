import numpy as np

a1 = np.arange(0, 60, 5).reshape(3, 4)
print(a1)
for x in np.nditer(a1):
    print(x)
print("-------------------------")
# 迭代的顺序匹配数组的内容布局，而不考虑特定的排序
for x in np.nditer(a1.T):
    print(x)
print("-------------------------")
# 以 C 风格顺序排序：
for x in np.nditer(a1.T.copy(order='C')):
    print(x)
print("-------------------------")
# 以 C 风格顺序排序：
for x in np.nditer(a1.T, order='C'):
    print(x)
print("-------------------------")
# 以读写模式修改元素的值
for x in np.nditer(a1, op_flags=['readwrite']):
    x[...] = 2 * x
print(a1)
print("-------------------------")
'''
flags 参数
c_index 可以跟踪 C 顺序的索引
f_index 可以跟踪 Fortran 顺序的索引
multi-index 每次迭代可以跟踪一种索引类型
external_loop 给出的值是具有多个值的一维数组，而不是零维数组
'''
for x in np.nditer(a1, flags=['external_loop'], order='F'):
    print(x)
print("-------------------------")
# 广播迭代
b = np.array([1, 2, 3, 4], dtype=int)
for x, y in np.nditer([a1, b]):
    print("%d:%d" % (x, y))
