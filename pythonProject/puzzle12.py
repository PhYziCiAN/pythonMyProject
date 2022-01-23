# Удалить вторую цифру трёхзначного числа

a = int(input('input your number from 100 to 999:\n'))
print((a // 100 * 10) + (a % 10))
