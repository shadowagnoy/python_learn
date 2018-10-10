import numpy as np

a1 = np.array([1, 2, 3, 4], dtype=np.float32)
print(a1)
print("数据类型", type(a1))
print("数组元素数据类型：", a1.dtype)
print("数组元素总数：", a1.size)
print("数组形状：", a1.shape)
print("数组的维度数目", a1.ndim)
print("数组的维度字节单位长度", a1.itemsize)
print("数组的flags", a1.flags)
a1.shape = (2, 2)  # 调整数组形状
a2 = a1.reshape(4, )  # reshape 来调整数组形状
print(a1)
print(a2)
