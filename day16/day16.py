#元组：不可修改的序列
x=1,2,3
print(x)


x=()
print(x)
#空元组用两个不包含任何内容的圆括号。

x=18,
y=(18,)
z=(18)
print(x,y,z)
#x,y表示只有一个值的元组,注z就代表数字18

x=3*(16+2)
print(x)

y=3*(16+2,)
print(y)

x=[1,2,3]
print(tuple(x))
x='abc'
print(tuple(x))
x=(1,2,3)
print(tuple(x))

x=1,2,3
print(x[1])

print(x[0:2])
print('\'****************')


def same(str):
    for x in str:
        count = str.count(x)
        if count>1:
            return False
        return True


if __name__ == '__main__':
    strs = 'leetcode'
    result = same(strs)
    print(strs + '有重复字符') if result else print(strs + '没有重复字符')