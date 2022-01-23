# Ввести номер четверти, показать диапазоны для возможных координат

a = int(input('Input number of quarter 1,2,3,4: '))

if a == 1:
    print('coordinates in this plane: \nx = 0 - 90,\ny = 0 - 90')
elif a == 2:
    print('coordinates in this plane: \nx = 0 - 90,\ny = 0 - (-90)')
elif a == 3:
    print('coordinates in this plane: \nx = 0 - -90,\ny = 0 - (-90)')
elif a == 4:
    print('coordinates in this plane: \nx = 0 - (-90),\ny = 0 - 90')
else:
    print('zero integer is not valid for input')
