# Написать программу вычисления значения функции y = f(a)

def func(a):
    y = a ** a
    return y


a = int(input('input your integer:\n'))
print(func(a))
