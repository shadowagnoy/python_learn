import numpy as np

a = np.array([0, 30, 45, 60, 90])
print(np.sin(a * np.pi / 180))  # 不同角度的正弦值
print(np.cos(a * np.pi / 180))  # 数组中角度的余弦值
print(np.tan(a * np.pi / 180))  # 数组中角度的正切值
'''
arcsin，arccos，和arctan函数返回给定角度的sin，cos和tan的反三角函数。 这些函数的结果可以通过numpy.degrees()函数通过将弧度制转换为角度制来验证
'''
print(np.degrees(np.arcsin(np.sin(a * np.pi / 180))))  # 计算角度的反正弦 转化为角度制
print(np.degrees(np.arccos(np.cos(a * np.pi / 180))))  # 计算角度的反余弦 转化为角度制
print(np.degrees(np.arctan(np.tan(a * np.pi / 180))))  # 计算角度的反正切 转化为角度制
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a))
print(np.around(a, decimals=1))  # decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
print(np.around(a, decimals=-1))
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.floor(a))  # 函数返回不大于输入参数的最大整数。 即标量x 的下限是最大的整数i ，使得i <= x。 注意在Python中，向下取整总是从 0 舍入
print(np.ceil(a))  # 输入值的上限，即，标量x的上限是最小的整数i ，使得i> = x
a = np.arange(9, dtype=np.float_).reshape(3, 3)
b = np.array([10, 10, 10])
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))
b = np.array([100], dtype=int)
print(np.reciprocal(b))  # 倒数
a = np.array([10, 100, 1000])
print(np.power(a, 2))
b = np.array([1, 2, 3])
print(np.power(a, b))  # 幂
print(np.mod(a, b))
print(np.remainder(a, b))  # 元素的除法余数。 函数numpy.remainder()也产生相同的结果
a = np.array([-5.6j, 0.2j, 11., 1 + 1j])
print(np.real(a))  # 复数类型参数的实部
print(np.imag(a))  # 复数类型参数的虚部
print(np.conj(a))  # 通过改变虚部的符号而获得的共轭复数
print(np.angle(a, deg=True))  # 参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示
