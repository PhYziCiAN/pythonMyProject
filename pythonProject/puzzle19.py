# Определить номер четверти плоскости,
# в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0


x = int(input('Input x from 1: '))
y = int(input('Input x from 1: '))

listQuarters = [1, 2, 3, 4]

if x > 0 and y > 0:
    print('coordinates in plane:', listQuarters[0])
elif x > 0 and y < 0:
    print('coordinates in plane:', listQuarters[1])
elif x < 0 and y < 0:
    print('coordinates in plane:', listQuarters[2])
elif x < 0 and y > 0:
    print('coordinates in plane:', listQuarters[3])
else:
    print('zero integer is not valid for input')

