# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов

fib1 = 0
fib2 = 1
list = [1,0,1]
n = 1
for i in range(5):
    n = fib1 + fib2
    fib1 = fib2
    fib2 = n
    list.append(n)
#print(list)

fib1 = 0
fib2 = 1
for i in range(5):
    n = fib1 - fib2
    fib1 = fib2
    fib2 = n
    list.insert(0,n)
print(list)