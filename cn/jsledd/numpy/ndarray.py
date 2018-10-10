import numpy as np

# numpy.array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0) 从数组中生成矩阵
'''
object : 数组类对象或者返回数组的方法
dtype  : 数组的所需数据类型，可选
copy   : 默认为True，对象是否被复制,可选
order  : {'K', 'A', 'C', 'F'} 数组在内存的存放次序，K:尽可能和原数组一致,A:如果原数组是列相邻，按列存储，C:按行，F:按列
subok  : 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类
ndmin  : 数组的最小维数
'''
ndarray1 = np.array([1, 2, 3])  # 一维数组
ndarray2 = np.array([[1, 2, 3], [4, 5, 6]])  # 二维数组
ndarray3 = np.array([1, 2, 3], ndmin=2)  # 最少是二维数组
ndarray4 = np.array([1, 2, 3], dtype=np.int32)  # 指定数组数据类型是整型
print(ndarray1)
print(ndarray2)
print(ndarray3)
print(ndarray4)
# numpy.empty(shape, dtype=None, order='C') 生成空矩阵
'''
shape  : 矩阵形状,整型元组或者整数
'''
ndarray5 = np.empty([2, 2])
print(ndarray5)
# numpy.empty_like(prototype, dtype=None, order='K', subok=True) 按之前的矩阵，仿照一个新的矩阵
'''
prototype:仿照的矩阵,按仿照矩阵的类型生成新矩阵
'''
ndarray6 = np.empty_like(ndarray5)  # 仿照之前矩阵，生成新矩阵
print(ndarray6)
# numpy.eye(N, M=None, k=0, dtype=float, order='C') 生成对角矩阵（主对角线上元素都为1，其他元素都为0
# numpy.identity(n, dtype=None) # 生成对角矩阵
'''
N  : 行数
M  : 列数，可以不写，默认和行相等
k  : 对角线偏移量，正数向右上方偏移，负数向左下方偏移
'''
ndarray7 = np.eye(4, 5)  # 生成4*5对角矩阵
ndarray8 = np.eye(4, k=1)  # 生成4*4对角矩阵,对角线向上偏移一位
ndarray9 = np.identity(4)  # 生成4*4对角矩阵
print(ndarray7)
print(ndarray8)
print(ndarray9)

# numpy.ones(shape, dtype=None, order='C') 生成指定形状的矩阵,内容填充1
# numpy.ones_like(shape, dtype=None, order='C') 仿照之前的矩阵,内容填充1
# numpy.zeros(shape, dtype=None, order='C') 生成指定形状的矩阵,内容填充0
# numpy.zeros_like(shape, dtype=None, order='C') 仿照之前的矩阵,内容填充0
# numpy.full(shape, fill_value, dtype=None, order='C') 生成指定形状的矩阵,内容填充fill_value
# numpy.full_like(shape, fill_value, dtype=None, order='C') 仿照之前的矩阵,内容填充fill_value
ndarray10 = np.ones(5)
ndarray11 = np.ones_like(ndarray10)
print(ndarray10)
print(ndarray11)
ndarray12 = np.zeros(4)
ndarray13 = np.zeros_like(ndarray10)
print(ndarray12)
print(ndarray13)
ndarray14 = np.full((4,), fill_value="www.jsledd.cn")
ndarray15 = np.full_like(ndarray10, fill_value=1)
print(ndarray12)
print(ndarray13)

# numpy.frombuffer(buffer, dtype=None, count=-1, offset=0) frombuffer将data以流的形式读入转化成ndarray对象
'''
buffer  : 任何暴露缓冲区借口的对象
count  : 需要读取的数据数量，默认为-1，读取所有数据
offset  : 需要读取的起始位置，默认为0
'''
ndarray16 = np.frombuffer(b'www.jsledd.cn', dtype='S1')
print(ndarray16)
# numpy.fromiter(iterable, dtype, count=-1) 可迭代对象生成新的一维数组
'''
iterable 可迭代对象
'''
ndarray17 = np.fromiter(iter(range(5)), dtype=float)
print(ndarray17)
# numpy.arange(start=None, stop=None, step=None, dtype=None) 从数值范围创建数组
'''
start  : 范围的起始值，默认为0
stop  : 范围的终止值（不包含）
step  : 两个值的间隔，默认为1
'''
ndarray18 = np.arange(10, 50, 3)
print(ndarray18)

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) 此函数类似于arange()函数。
# 在此函数中，指定了范围之间的均匀间隔数量，而不是步长
'''
stop  : 序列的终止值，如果endpoint为true，该值包含于序列中
num  : 要生成的等间隔样例数量，默认为50
endpoint  : 序列中是否包含stop值，默认为ture
retstep  : 如果为true，返回样例，以及连续数字之间的步长
'''
ndarray19 = np.linspace(10, 20, 5)
ndarray20 = np.linspace(10, 20, 5, endpoint=False)
print(ndarray19)
print(ndarray20)
x = np.linspace(1, 2, 5, retstep=True)
print(x)
# numpy.logscale(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# 此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10
'''
start  : 起始值是base ** start
stop  : 起始值是base ** stop
endpoint  : 如果为true，终止值包含在输出数组当中
base  : 对数空间的底数，默认为10
'''
ndarray21 = np.logspace(1.0, 2.0, num=10)
ndarray22 = np.logspace(1, 10, num=10, base=2)
print(ndarray21)
print(ndarray22)
