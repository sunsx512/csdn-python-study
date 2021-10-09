#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   day19.py    
@Contact :   sunsx.sun@advantech.com.cn
@License :   

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/7/5 15:19   sunsx.sun      1.0         None
'''

# import lib

from math import pi

str17 = "{num:10}".format(num=3)
print(str17)
str18 = "{name:10}".format(name="Bob")
print(str18)

str19 = "{pi:10.2f}".format(pi=pi)
print(str19)

str20 = "{:.5}".format("Guido van Rossum")
print(str20)

str21 = "One googol is {:,}".format(10**100)
print(str21)

str22 = '{:010.2f}'.format(pi)
print(str22)

str23 = '{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi)
print(str23)

str24 = '{0:$<10.2f}\n{0:$^10.2f}\n{0:$>10.2f}'.format(pi)
print(str24)

str25 = '{0:10.2f}\n{1:10.2f}'.format(pi,-pi)
print(str25)

str26 = '{0:10.2f}\n{1:=10.2f}'.format(pi,-pi)
print(str26)

str27 = '{0:.2}\n{1:.2}'.format(pi,-pi)
print(str27)

str28 = '{0:+.2}\n{1:+.2}'.format(pi,-pi)
print(str28)

str29 = '{0: .2}\n{1: .2}'.format(pi,-pi)
print(str29)

str30 = "{:b}".format(42)
print(str30)
str31 = "{:#b}".format(42)
print(str31)

str32 = "{:g}".format(42)
print(str32)
str33 = "{:#g}".format(42)
print(str33)


#代码清单
#根据指定的宽度打印格式良好的价格列表
print('------------下面是代码清单--------------')
width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width,price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)

print('='*width)
print(header_fmt.format('Item','Price'))
print('-'*width)

print(fmt.format('Apples',0.4))
print(fmt.format('Pears',0.5))
print(fmt.format('Cantaloupes',1.92))
print(fmt.format('Dried Apricots (16 oz.)',8))
print(fmt.format('Prunes (4 lbs.)',12))

print('=' * width)
