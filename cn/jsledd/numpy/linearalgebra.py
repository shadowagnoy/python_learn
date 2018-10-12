import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))  # 数组的点积 [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
print(np.vdot(a, b))  # np.vdot(a,b) 1*11 + 2*12 + 3*13 + 4*14 = 130
print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))  # 一维数组的向量内积
print(np.inner(a, b))  # 数组的向量内积 1*11+2*12, 1*13+2*14  3*11+4*12, 3*13+4*14
print(np.matmul(a, b))  # 对于二维数组，它就是矩阵乘法
b = [1, 2]
print(np.matmul(a, b))  # 二维和一维运算,任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除
c = np.arange(8).reshape(2, 2, 2)
b = np.arange(4).reshape(2, 2)
print(np.matmul(c, b))  # 将其视为存在于最后两个索引的矩阵的栈，并进行相应广播
print(np.linalg.det(a))  # 对于 2×2 矩阵，它是左上和右下元素的乘积与其他两个的乘积的差 行列式计算为1*4-2*3
d = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(np.linalg.det(d))  # 6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2)
'''
线性方程
x + y + z = 6
2y + 5z = -4
2x + 5y - z = 27
未知数的系数写下来，排列成一个矩阵A [[1,1,1],[0,2,5],[2,5,-1]]
常数项构成一个一维数组(向量) B:[6,-4,27]
未知向量 X:[x,y,z]
方程变成 AX=B 或 A^(-1)B
带入矩阵参数a指的是系数矩阵，参数b指的是常数项矩阵
'''
A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
B = [6, -4, 27]
print(np.linalg.solve(A, B))
y = np.linalg.inv(A)  # 矩阵A的逆
print(np.dot(y, B))  # solve dot 关系
