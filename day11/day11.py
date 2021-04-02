print('00000')
# 上一节回顾
# 索引操作示例

# 将以数指定年、月、日的日期打印出来。
months=['January','February','March','April','May','June','July','August','September','October','November','December']

# 一个列表，其中含有数1~31对应的结尾
endings=['st','nd','rd']+17*['th']\
    +['st','nd','rd']+7*['th']\
    +['st']

print(endings)
print('******************************************************')

year=input('Year:')
month=input('Month(1~12):')
day=input('Day(1~31):')

month_number = int(month)
day_number = int(day)

#别忘了将表示月和日的数减1，这样才能得到正确的索引
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name+' '+ordinal+', '+year)

#2.2.2切片
tag = '<a href="http://www.python.org">Python Web site </a>'
print(tag[-1])
str1 = tag[9:30]
print(str1)
str2 = tag[32:-4]
print(str2)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[0:1])
# 简写 获取8，9，10
print(numbers[-3:-1])

print(numbers[-3:0]) #空序列

print(numbers[-3:]) #取后三个元素
print(numbers[:3]) #取前三个元素
print(numbers[:]) #复制整个序列

print('******************************************************')
# 切片操作示例
# 代码清单002
# 需求：输入网址，提取域名
url = input('Please enter the URL：')
print('Domain name:  '+url[11:-4])

print('*************************步长操作*****************************')
# 步长
print(numbers[0:10]) #提取原序列
print(numbers[:]) #提取原序列,简写
print(numbers[0:10:1]) #提取原序列,步长为1
print(numbers[0:10:2]) #提取步长为2的序列
print(numbers[::2]) #提取步长为2的序列，简写
print(numbers[0:10:3]) #提取步长为3的序列
print(numbers[::3]) #提取步长为3的序列，简写

# 步长不能为0，否则无法向前移动，但可以为负数（从右向左提取元素）
#print(numbers[::0])
print(numbers[::-3])

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[6:3])
print(numbers[6:3:-1])