# cmath和复数

#from math import sqrt
#sqrt(-1)
'''
Traceback (most recent call last):
  File "F:/PythonStudy/csdn/day4/day4.py", line 3, in <module>
    sqrt(-1)
ValueError: math domain error

复数的平方根，报错，有些显示 
sqrt(-1)=nan
"nan"有特殊含义，指的是 “非数值”

如果我们坚持将值域限定为实数，并使用其近似的浮点数实现，就无法计算负数的平方根。
负数的平方根为虚数，而由实部和虚部组成的数为**复数**，Python提供了一个专门用于处理复数的模块。

'''
import cmath

print(cmath.sqrt(-1))

'''
注意这里没有使用from...import.
如果使用这种import命令，将无法使用常规函数sqrt，因此除非必须使用from版的import命令，否则应坚持使用常规版的import命令。

1j是个虚数，虚数都以j或J结尾。
复数的算数运算都基于如下定义：
    -1的平方根是1j
'''
x=(1+3j)*(9+4j)
print(x)