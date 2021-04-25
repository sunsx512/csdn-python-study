#列表方法
#append
lst = [1,2,3]
lst.append(4)
print(lst)

lst = [1,2,3]
lst.clear()
print(lst)

a=[1,2,3]
b=a
b[1]=4
print(a)

a=[1,2,3]
b=a.copy()
b[1]=4
print(a)
print(b)

ax=['a','b','c','d','a']
print(ax.count('a'))

x=[[1,2],1,1,[2,1,[1,2]]]
print(x.count(1))
print(x.count([1,2]))

a=[1,2,6]
b=[4,5,3]
c1=a.extend(b)
c2=a
print(a)
print(b)
print(c1)
print(c2)

print('************************')
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a)
print('************************')

a=[1,2,3]
b=[4,5,6]
print(a[3:])
a[len(a):]=b
print(a)
print('++++++++++++++++++++++++++++++')

knights = ['we','are','the','knights','who','say','ni']
print(knights.index('who'))

numbers1 = [1,2,3,4,5,6,7]
numbers1.insert(3,'hello')
print(numbers1)

numbers2 = [1,2,3,4,5,6,7]
numbers2[3:3]=['hello']
print(numbers2)

print('++++++++++++++++++++++++++++++')
x=[1,2,3]
print(x.pop())
print(x)

x.pop(0)
print(x)

x=[1,2,3]
x.append(x.pop())
print(x)
print('++++++++++++++++++++++++++++++')


x=['to','be','or','not','to','be']
x.remove('be')
print(x)
print('111111111111111111111111111111')

x=[1,2,3,5,4]
x.reverse()
print(x)
print('++++++++++++++++++++++++++++++')
x=[1,2,3,4,5]
print(list(x))
print(list(reversed(x)))
print('++++++++++++++++++++++++++++++')
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


print('++++++++++++++++++++++++++++++')
x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)
print(x)

x = [4,5,1,2,7]
x.sort(reverse=True)
print(x)