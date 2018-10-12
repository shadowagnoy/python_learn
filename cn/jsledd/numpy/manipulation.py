import numpy as np

a1 = np.arange(2, 10)
a2 = a1.reshape(4, 2)  # 修改形状
print(a2)
print(a2.flat[5])  # 返回展开数组中的下标的对应元素 (一维迭代器)
print(a2.flatten(order='F'))  # 以 F 风格顺序展开的数组 返回一维的数组副本
print(a2.ravel(order='F'))  # 以 F 风格顺序展开的数组 并且按需生成副本
print(np.transpose(a2))  # numpy.ndarray.T 功能相同
print("------------------------------------")
a3 = np.arange(8).reshape(2, 2, 2)
print(a3)
print(np.rollaxis(a3, 2))  # 将轴 2 滚动到轴 0（宽度到深度）
print(np.rollaxis(a3, 2, 1))  # 将轴 0 滚动到轴 1：（宽度到高度）
print(np.swapaxes(a3, 2, 0))  # 现在交换轴 0（深度方向）到轴 2（宽度方向）
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
b = np.broadcast(x, y)  # 对 y 广播 x.它拥有 iterator 属性，基于自身组件的迭代器元组
r, c = b.iters
print(b.shape)
c = np.empty(b.shape)
c.flat = [u + v for (u, v) in b]
print(c)
print(x + y)  # 获得了和 NumPy 内建的广播支持相同的结果
print(np.broadcast_to(b, (4, 4)))  # 此函数将数组广播到新形状
x = np.array(([1, 2], [3, 4]))
y = np.expand_dims(x, axis=1)
print(x.shape, y.shape)  # 函数通过在指定位置插入新的轴来扩展数组形状
x = np.arange(9).reshape(1, 3, 3)
y = np.squeeze(x)
print(y.shape)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(np.concatenate((x, y)))  # 此函数用于沿指定轴连接相同形状的两个或多个数组
print(np.concatenate((x, y), axis=1))
print(np.stack((x, y), 0))  # 沿轴 0 堆叠两个数组
print(np.stack((x, y), 1))  # 沿轴 1 堆叠两个数组
print(np.hstack((x, y)))  # 水平堆叠两个数组
print(np.vstack((x, y)))  # 竖直堆叠两个数组
a = np.arange(9)
print(np.split(a, 3))  # np.split(a,[4,7])
print(np.split(a, [4, 7]))  # 将数组在一维数组中表明的位置分割
a = np.arange(16).reshape(4, 4)
print(np.hsplit(a, 2))  # split()函数的特例，其中轴为 1 表示水平分割，无论输入数组的维度是什么
print(np.vsplit(a, 2))  # split()函数的特例，其中轴为 0 表示竖直分割，无论输入数组的维度是什么
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.resize(a, (3, 2)))
print(np.resize(a, (3, 4)))  # 尺寸变大了 出现重复元素
print(np.append(a, [7, 8, 9]))  # 向数组添加元素
print(np.append(a, [[7, 8, 9]], axis=0))  # 沿轴 0 添加元素
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))  # 沿轴 1 添加元素
a = np.array([[1, 2], [3, 4], [5, 6]])
print(np.insert(a, 3, [11, 12]))  # '未传递 Axis 参数。 在插入之前输入数组会被展开
print(np.insert(a, 1, [11], axis=0))  # 沿轴 0 广播
print(np.insert(a, 1, [11], axis=1))  # 沿轴 1 广播
a = np.arange(12).reshape(3, 4)
print(np.delete(a, 5))  # 未传递 Axis 参数。 在插入之前输入数组会被展开
print(np.delete(a, 1, axis=1))  # 删除第二列
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))  # 包含从数组中删除的替代值的切片
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print(np.unique(a))
print(np.unique(a, return_index=True))  # 去重数组的索引数组
print(np.unique(a, return_inverse=True))  # 使用下标重构原数组
print(np.unique(a, return_counts=True))  # 去重元素的重复数量
print(np.bitwise_and(13, 17))  # 位与
print(np.bitwise_or(13, 17))  # 位或
print(np.invert(np.array([13], dtype=np.uint8)))  # 13 的位反转，其中 ndarray 的 dtype 是 uint8
print(np.left_shift(10, 2))  # 将 10 左移两位
print(np.right_shift(40, 2))  # 将 40 左移两位
