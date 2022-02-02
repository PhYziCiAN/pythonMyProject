# Реализовать алгоритм перемешивания списка.

import datetime
import random


# x = [1,2,3,4,5,6,7,8,9,10]

# def mixer (x):
#     for i in range (len(x)-1):
#         index  = random.randint(i+1, len(x)-1)
#         x[i], x[index] = x[index], x[i]
#         return x
# print(x)
# print(mixer(x))

def rndTime(n):
    y = range(1,n,2)
    for item in y:
        #item = datetime.datetime.now().microsecond%10+1
        return item
print(rndTime(6))