# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random

a = random.randrange(10, 100, 1)
print('Checked number: ', a)
b = a % 10
c = a // 10
print('Max is: ', max(c, b))
