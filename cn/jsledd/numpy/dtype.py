import numpy as np

# numpy.dtype(self, obj, align=False, copy=False)
'''
obj  : 被转换为数据类型的对象。
align: 如果为true，则向字段添加间隔，使其类似 C 的结构体
copy : 生成dtype对象的新副本，如果为flase，结果是内建数据类型对象的引用。 
'''
dt1 = np.dtype(np.int32)  # 使用数组标量类型
dt2 = np.dtype('i4')  # int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他
dt3 = np.dtype('>i4')  # 使用端记号
dt4 = np.dtype([('age', np.int8)])  # 创建结构化数据类型
arr = np.arange(5)
dt5 = arr.astype(np.float64)  # 数据类型转换 !!!不能使用 arr.dtype = 'float64'!!!
ndarray1 = np.array([(10,), (20,), (30,)], dtype=dt4)  # 应用于 ndarray 对象
studentdt = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
student = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=studentdt)
print(dt5)
print(ndarray1['age'])
print(studentdt)
print(student['name'])
