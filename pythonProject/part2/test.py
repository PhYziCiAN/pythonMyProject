# def math(op, x):
#     print(op(x))

# def cal1(x):
#     return x*11

# f = lambda a, b: a*b
# print(f(4, 5))

# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# list = [i f or i in range(1,21) if i%2 ==0]
# print(list)
<<<<<<< HEAD
path = 'numbers.txt'
=======
path = 'G:/Мой диск/Learn_GB/Python/pythonProject/part2/numbers.txt'
>>>>>>> a15625ee115f2555f51d337e4b0dedf20e24fbf6
h = open(path,'r')
data = h.read()
h.close()
# space_pos = data.index(' ')
# print(space_pos)
numbers = []
while data!=' ':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos:]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e%2:
        out.append((e, e*2))
print(out)