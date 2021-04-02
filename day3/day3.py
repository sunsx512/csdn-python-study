import math
#模块

x=math.floor(32.9)
print(x)

x=math.ceil(32.9)
print(x)

'''
>>> floor(32.9)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    floor(32.9)
NameError: name 'floor' is not defined
'''

x=int(32.9)
print(x)
# ceil()上取整函数，floor()下取整函数，在模块math中，无法直接使用，需使用关键字import引入。
# 不指定模块前缀调用。

from math import floor
print(floor(32.9))

from  math import  ceil
print(ceil(32.9))

from math import  sqrt
print(sqrt(9))