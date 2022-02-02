# Cтрока содержит набор чисел. Показать большее и меньшее число

#str = '5 7 19 15'
def someFunc(str):

    str = str.split()
    list1 = []
    for j in str:
        list1.append (int(j))
    return (max(list1), min(list1))
print(someFunc('5 7 19 15'))