# Написать программу замену элементов массива на противоположные


arrInt1 = (list((range(1, 11, 1))))
print(arrInt1)


def rem1(arrInt1):
    for j in arrInt1:
        arrInt1[j] = - arrInt1[j]
    return arrInt1


print(rem1(arrInt1))
