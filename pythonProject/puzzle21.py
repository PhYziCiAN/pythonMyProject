# Программа проверяет пятизначное число на палиндромом.
import string

dig_check = input('Input 5-digits number: ')
print(dig_check)

if dig_check[0] == dig_check[4] and dig_check[1] == dig_check[3]:
    print('Your integer', dig_check, 'is palindrome')
else:
    print('Your integer', dig_check, "is not palindrome")
