#概念：
'''
**1、算法**：算法犹如菜谱，告诉你如何完成特定的任务。从本质上说，编写计算机程序就是使用计算机能够理解的语言（如Python）描述一种算法。这种对机器友好的描述被称为**程序**，主要由**表达式**和**语句**组成。
<br>
**2、表达式**：表达式为程序的一部分，结果为一个值。如：2+2就是一个表达式，结果为4。简单表达式是使用**运算符**（如+、*）和**函数**（如pow）将**字面值**（如2或“Hello”）组合起来得到的。通过组合简单的表达式，可创建复杂的表达式，如（2+2）*（3-1）。表达式还可能包含**变量**。
<br>
**3、变量**：变量是表示值的名称。通过**赋值**，可将新值赋给变量，如x=2。赋值是一种**语句**。
<br>
**4、语句**：语句是让计算机执行特定操作的指示。这种操作可能是修改变量（通过赋值）、将信息打印到屏幕上（如print("Hello,world!")）、导入模块或执行众多其他任务。
<br>
**5、函数**：Python函数类似于数学函数，它们可能接受参数，并返回结果（在第六章学习编写自定义函数时，你将发现函数实际上可以在返回前做很多事情）。
<br>
**6、模块**：模块是扩展，可通过导入它们来扩展Python的功能。如：模块math包含多个很有用的函数。
<br>
**7、程序**：你通过练习学习了如何编写、保存和运行Python程序。
<br>
**8、字符串**：字符串非常简单。它们其实就是一段文本，其中的字符是用Unicode码点表示的。

'''
#函数：
#print(abs(-10))

a=bytes([1,2,3,4])
print(a)

import cmath as a
print(a.sqrt(-1))
print(a.sqrt(9))

stra='1111'
x=100
f1=float(stra)
print(f1)
f2=float(x)
print(f2)
print(f1+f2)

#str=help()
#print(str)

stra=input('你的名字是：')
print(stra)

stra='999'
f=1.0
i1=int(stra)
i2=int(f)
print(i1)
print(i2)
print(i1+i2)

import math as a
print(a.ceil(0.4))
print(a.ceil(-0.4))
print(a.floor(0.4))
print(a.floor(-0.4))
print(a.sqrt(9))
#print(a.sqrt(-1))

print(pow(2 ,3))

a=1
b='1'
print(a,b)

x='123456'
print(repr(x))

a=3.1415926
print(round(a,2))
b=2.5
print(round(b))

y='"Hello world!" \nshe said'
print(repr(y))
print(str(y))
