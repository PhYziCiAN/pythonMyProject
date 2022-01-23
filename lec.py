
from re import S


value = None
#print(type(value))
a = 123
b = 1.23
#print(type(a))
#print(type(b))
value = 12334

s = 'hello world'
s = 'hello \nworld'
s = "hello 'world"
print(s) # output string

print(a, '-',b,'-',s)
print('{1} -{2}-{0}'.format (a,b,s))
print(f'{a} -{b}-{s}')

f = True
print(f)
list = ['1','2','3']
print(list)
print('Input a')
a = input()
a = int(input()) # maybe float or int or other type
e = 23.3
d = -5
32
c = round(e*d,5)
print(c)

if e > d:
    print(e)
else:
    print(d) #elif
while e!=0:
    print(e)


def f(x):
    if x==1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return