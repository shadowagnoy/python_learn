import pandas as pd
import numpy as np

# Create a Dictionary of series
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

# Create a DataFrame
df = pd.DataFrame(d)
print(df.sum())  # 请求轴的值的总和。 默认情况下，轴为索引(axis=0)
print(df.sum(1))
print(df.mean())  # 平均值
print(df.std())  # 数字列的Bressel标准偏差
print(df.describe())  # 汇总数据
print(df.describe(include=['number']))  # object - 汇总字符串列,number - 汇总数字列,all - 将所有列汇总在一起(不应将其作为列表值传递)
