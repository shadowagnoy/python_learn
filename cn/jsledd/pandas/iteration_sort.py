import pandas as pd
import numpy as np

N = 20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})

for col in df:
    print(col)
df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
for key, value in df.iteritems():  # 迭代(key，value)对
    print(key, value)
for row_index, row in df.iterrows():  # 将行迭代为(索引，系列)对
    print(row_index, row)
for row in df.itertuples():  # 以namedtuples的形式迭代行
    print(row)
print("---------------------------------------------------------")
unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
sorted_df = unsorted_df.sort_index()
print(sorted_df)
print(unsorted_df.sort_index())  # 按标签排序
print(unsorted_df.sort_index(ascending=False))  # 按标签排序
print(unsorted_df.sort_index(axis=1))
print(unsorted_df.sort_values(by='col1'))  # 按值排序
print(unsorted_df.sort_values(by=['col1', 'col2']))
print(unsorted_df.sort_values(by='col1', kind='mergesort'))  # mergeesort，heapsort和quicksort 其中Mergesort 是唯一稳定的
