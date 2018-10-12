import numpy as np

X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])
n = 4
print(np.mod(X, 1) == 0)
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=1)
M &= (X.sum(axis=-1) == n)
print(X[M])
