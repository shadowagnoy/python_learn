import pandas as pd

df = pd.DataFrame()  # 创建一个空的dataframe
data = [1, 2, 3, 4, 5]
df1 = pd.DataFrame(data)
print(df1)  # 使用单列表创建
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df2 = pd.DataFrame(data, columns=['Name', 'Age'])
print(df2)  # 使用列表的列表创建
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df3 = pd.DataFrame(data)
print(df3)  # 从ndarrays/Lists的字典来创建DataFrame
df4 = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df4)  # 创建一个索引的数据帧(DataFrame)
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data))  # 字典列表 创建
print(pd.DataFrame(data, index=['first', 'second']))
df5 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df5)  # 列不存在 附加上 NaN
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df6 = pd.DataFrame(d)
print(df6)  # 字典的系列
print("-----------------------------------------------")
print(df6['one'])  # 选择列
df6['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # 列添加
df6['four'] = df6['one'] + df6['three']  # 列组合添加
print(df6)
del (df6['four'])  # 列删除
df6.pop('three')  # 列弹出
print(df6)
print("-----------------------------------------------")
print(df6.loc['b'])  # 行选择
print(df6.iloc[2])  # 按整数位置选择
print(print(df6[2:4]))  # 使用切片选择行
df7 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df8 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
print(df7.append(df8))  # 附加行
print(df6.drop('a'))  # 删除行
