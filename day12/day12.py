print('序列相加')

arr1 = [1,2,3]
arr2 = [4,5,6]
print(arr1+arr2)

arr3 = 'Hello,'
arr4 = 'World!'
print(arr3+arr4)

#print(arr1+arr4)

#乘法
arr1 = 'Hello'
print(arr1*5)
arr2 = [3,4]
print(arr2*10)

arr3=[0]
print(arr3*10)

sequence = [None]*10
print(sequence)

#代码清单2-3

sentence = input("Sentence: ")
screen_width = 30
text_width = len(sentence)
box_width = text_width+4
left_margin = (screen_width - box_width)//2

print()
print(' '*left_margin+'+' +'_'*(box_width-2) +  '+')
print(' '*left_margin+'| '+' '*text_width    + ' |')
print(' '*left_margin+'| '+    sentence      + ' |')
print(' '*left_margin+'| '+' '*text_width    + ' |')
print(' '*left_margin+'+' +'_'*(box_width-2) +  '+')
print()
