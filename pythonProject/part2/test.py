def math(op, x):
    print(op(x))

def cal1(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
calc(lambda x, y: x*y, 6, 7)
f = lambda a, b: a*b

def f(x):
    return x**2
list = [(i,f(i)) for i in range(1, 21) if i % 5 == 0]
print(list)
# print(f(4, 5))

# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# list = [i f or i in range(1,21) if i%2 ==0]
# print(list)
# path = 'G:/Мой диск/Learn_GB/Python/pythonProject/part2/numbers.txt'
# h = open(path,'r')
# data = h.read()
# h.close()
# space_pos = data.index(' ')
# print(space_pos)
# numbers = []
# while data!=' ':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos:]))
#     data = data[space_pos+1:]
# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e*2))
# print(out)