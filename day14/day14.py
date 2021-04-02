#列表
strlist = list('Hello')
print(strlist)

print(''.join(strlist))

#1、修改元素：给元素赋值。
x = [1,1,1]
x[1] = 2
print(x)

names = ['张三','李四','王五','赵六']
del names[1]
print(names)

name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

name = list('Perl')
name[1:] = list('ython')
print(name)

numbers = [1,5]
print(numbers[1:1])
numbers[1:1] = [2,3,4]
print(numbers)
numbers[1:4] = []
print(numbers)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(nums[0::2])
nums[0::2] = [0,0,0,0,0,0,0,0]
print(nums)