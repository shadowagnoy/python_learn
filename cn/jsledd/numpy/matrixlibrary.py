import numpy.matlib
import numpy as np

print(np.matlib.empty((2, 2)))  # 填充为随机数据
print(np.matlib.zeros((2, 2)))
print(np.matlib.ones((2, 2)))
print(np.matlib.eye(n=3, M=4, k=0, dtype=float))
print(np.matlib.identity(5, dtype=float))
print(np.matlib.rand(3, 3))
i = np.matrix('1,2;3,4')
print(np.asarray(i))
print(np.asmatrix(i))
