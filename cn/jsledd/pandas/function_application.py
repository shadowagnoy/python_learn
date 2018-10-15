import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df.pipe(lambda x, y: x + y, 20))  # df.pipe(adder, 20)
print(df.apply(np.mean, axis=1))  # 按行执行
print(df.apply(lambda x: x.max() - x.min()))  # 默认按列执行
print(df['col1'].map(lambda x: x * 100))
print(df.applymap(lambda x: x * 100))
