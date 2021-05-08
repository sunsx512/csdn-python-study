#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   day18.py    
@Contact :   sunsx.sun@advantech.com.cn
@License :   

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/25 17:50   sunsx.sun      1.0         None
'''

# import lib
#3.1 字符串的基本操作。
#所有的元素赋值和切片赋值都是非法的
website = 'http://www.python.org'
print(website[-3:])
#website[-3:] = 'com' #无法进行切片赋值

format = "Hello ,%s . %s enough for ya?"
values = ('world','Hot')
print(format % values)

from string import  Template
tmp1 = Template("Helllo, $who! $what enough for ya?")
print(tmp1.substitute(who="Mars",what="Dusty"))

str1 = "{}，{} and {}".format("first","second","third")
print("str1=   "+str1)

str2 = "{0}，{1} and {2}".format("first","second","third")
print("str2=   "+str2)

str3 = "{3} {0} {1} {2} {3} {0}".format("be","or","not","to")
print("str3=   "+str3)

from math import pi
str4 = "{name} is approximately {value:.2f}.".format(value=pi,name="π")
print("str4=   "+str4)
