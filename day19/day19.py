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