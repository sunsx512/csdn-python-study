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
#
# from math import pi
# str4 = "{name} is approximately {value:.2f}.".format(value=pi,name="π")
# print("str4=   "+str4)

from math import pi
str5 = "{name} is approximately {value}.".format(value=pi,name="π")
print("str5=   "+str5)

name = '张三'
str6 = f'The boy is {name}'
print(str6)

str7 = "{{ceci n'est pas une replacement field}}"
print(str7)
str8 = "{{ceci n'est pas une replacement field}}".format()
print(str8)

str9 = "{foo}{}{bar}{}".format(1,2,bar=4,foo=3)
print(str9)

str10 = "{foo}{1}{bar}{0}".format(1,2,bar=4,foo=3)
print(str10)

fullname = ["Alfred","Smoketoomuch"]
str11 = "Mr {name[1]}".format(name=fullname)
print(str11)

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
tmpl.format(mod=math)
print(tmpl)


import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
tmpl2=tmpl.format(mod=math)
print(tmpl2)

str13 = "{pi!s} {pi!r} {pi!a}".format(pi="π")
print(str13)

str14 = 'the number is {num}'.format(num=42)
print(str14)
str15 = 'the number is {num:f}'.format(num=42)
print(str15)
str16 = 'the number is {num:b}'.format(num=42)
print(str16)




