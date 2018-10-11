import numpy as np

a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
a2 = np.array([10, 20, 30, 40])
a3 = np.array([[1, 2], [3, 4]])
a4 = np.array([[10, 20], [30, 40]])
print(a1 * 6)
print(a1 * a2)  # 对应元素相城
print(np.dot(a3, a4))  # 矩阵乘
