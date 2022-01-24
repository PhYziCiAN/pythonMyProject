#Найти произведение пар чисел в одномерном массиве. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.
from random import randint

lis = [randint(10, 100) for i in range(6)]
print(lis)

def multi(lis):
    lis1 = []
    for i in range(len(lis) // 2):
        lis1.append(lis[i] * lis[len(lis) - i - 1])
    return lis1

print(multi(lis))