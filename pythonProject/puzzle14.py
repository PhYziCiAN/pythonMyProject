# Найти третью цифру числа или сообщить, что её нет

a = int(input('input your number from 10 to 999:\n'))
if a > 99:
    print('third digit in integer is:', a % 10)
else:
    print('input integer contain only 2 digits, third digit do not exist')
