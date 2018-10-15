import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4))
print(s.axes)  # Series 的标签列表
print(s.empty)  # 判断是不是空值
print(s.ndim)  # 判断数据维度
print(s.size)  # 判断元素个数
print(s.values)  # 返回数据值
print(s.head(2))  # 小样品提取 开始2行 默认5
print(s.tail(2))  # 小样品提取 末尾2行 默认5
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}

df = pd.DataFrame(d)
print(df.T)  # 行列装换
print(df.axes)  # 行轴标签和列轴标签列表
print(df.dtypes)  # 数据类型
print(df.shape)
