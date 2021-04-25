#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   day17.py    
@Contact :   sunsx.sun@advantech.com.cn
@License :   

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/25 16:02   sunsx.sun      1.0         None
'''

# import lib

str = '123456789'
print(len(str))

str = '123456789'
print(list(str))


print(max(0,1,2,5))
print(ord('A'),ord('a'),chr(65),chr(97),max('A','a'))

print(min(0,1,2,5))
print(ord('A'),ord('a'),chr(65),chr(97),min('A','a'))


x=[1,2,3,5,4]
x.reverse()
print(x)

x=[1,2,3,4,5]
print(list(x))
print(list(reversed(x)))

x = [4,5,1,2,7]
x.sort()
print(x)
# sort()没有返回值，所以不可用y=x.sort()
x = [4,5,1,2,7]
y=x.sort()
print(y)

# 正确的方法是要将y关联到x的副本
x = [4,5,1,2,7]
y = x.copy()
y.sort()
print(x,y)

# 另一种方法使用函数sorted()
x = [4,5,1,2,7]
y = sorted(x)
print(x,y)

# sorted可用于任何序列，但总是返回一个列表
x = sorted('Python')
print(x)


x=[1,2,3]
print(tuple(x))
x='abc'
print(tuple(x))
x=(1,2,3)
print(tuple(x))
