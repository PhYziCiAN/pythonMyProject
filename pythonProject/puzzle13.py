# Выяснить, кратно ли число заданному, если нет, вывести остаток.

import random

a = random.randrange(10, 100, 1)
b = int(input('input your number from 2 to 10:\n'))

if a % b == 0:
    print('user integer is multiple of random integer')
else:
    print(a, '\n', a % b)
