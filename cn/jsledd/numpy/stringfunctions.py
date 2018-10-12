import numpy as np

print(np.char.add(['hello'], ['jsledd']))
print(np.char.multiply('Hello ', 3))
print(np.char.center('hello', 20, fillchar='*'))  # 此函数返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充
print(np.char.capitalize('hello world'))  # 首字母大写
print(np.char.title('hello how are you?'))  # 字符串的按元素标题转换版本，其中每个单词的首字母都大写
print(np.char.lower(['HELLO', 'WORLD']))  # 元素转换为小写
print(np.char.upper('hello'))
print(np.char.split('www.jsledd.cn', sep='.'))
print(np.char.splitlines('hello\nhow are you?'))  # 元素的单词列表，以换行符分割'\n'，'\r'，'\r\n'都会用作换行符
print(np.char.strip(['arora', 'admin', 'java'], 'a'))  # 元素移除了开头或结尾处的特定字符
print(np.char.join([':', '-'], ['dmy', 'ymd']))
print(np.char.replace('He is a good boy', 'is', 'was'))
print(np.char.encode('hello', 'cp500'))
