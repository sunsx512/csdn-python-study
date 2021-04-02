#成员资格
print("Hello")

str1 = 'permissions'
str2 = 'rm'
str3 = 'x'
print(str2 in str1)
print(str3 in str1)

users = ['mlh','foo','bar']
login = input('Enter your user name: ') in users
print(login)

database = [
    ['albert','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843']
]

username = input('User name: ')
pin = input('PIN code: ')

if [username,pin] in database:
    print('Access granted')

numbers = [100,34,678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print('*********')
print(max(2,3,4,5,6))
print(min(-1,2,3,6,5))