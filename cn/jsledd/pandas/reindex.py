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
print(df)
# reindex the DataFrame
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(df_reindexed)
df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
print(df1)
print(df2.reindex_like(df1, method='ffill'))  # pad/ffill - 向前填充值 bfill/backfill - 向后填充值 nearest - 从最近的索引值填充
print(df2.reindex_like(df1, method='bfill', limit=1))  # pad/ffill - 向前填充值 bfill/backfill - 向后填充值 nearest - 从最近的索引值填充
print(df2.rename(columns={'col1': 'c1', 'col2': 'c2'}, index={0: 'apple', 1: 'banana', 2: 'durian'}))
