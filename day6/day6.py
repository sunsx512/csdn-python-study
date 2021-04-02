print('hello python')
'''
强大的海归绘图

编写简单实例时，print语句很有用，如果你要尝试提供更有趣的输出，应考虑使用模块“turtle”
它实现了海龟绘图法，如果你正在运行IDLE，就可以使用这个模块，他让你能够绘出图形而不是打出文本。

通常，应避免导入模块中所有的名称，但尝试海归绘图法时，这样做可提供极大的方便。

from turtle import *

确定使用哪些函数后，可回头调整import语句，以便只导入这些函数。

海归绘图法的理念源自形如海龟的机器人。这种机器人可前进，可后退，可向左，可向右旋转一定角度。
另外这种机器人还携带一支铅笔，可通过抬起或者放下来控制铅笔什么时候接触脚下的纸张。
模块turtle能让你模拟这样的机器人。例如，下面的代码演示如何绘制一个三角形。


'''

'''
import turtle
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
'''

'''
执行这些代码会出现一个新窗口，其中的一个箭头形“海龟”不断的移动，并留下轨迹。
将铅笔抬起，使用penup(),放下，使用pendown()

要了解其他命令请参阅“[Python库参考手册](https://docs.python.org/3/library/turtle.html)”
要了解如何绘图可在网上搜索海龟绘图法。
如：https://blog.csdn.net/qq_40843903/article/details/86583216
实现下彩色螺旋线的例子，很炫！

'''
import turtle as t
import time

t.pensize(2)
t.bgcolor('black')
colors = ['red','yellow','purple','blue']
t.tracer(False) #此条注释可看轨迹
for x in range(400):
    t.forward(2*x)#长度
    t.color(colors[x%4])#颜色
    t.left(91)#偏转角度
t.tracer(True)
time.sleep(1000)
t.done()

