# Дано число обозначающее день года. Выяснить является ли день недели выходным днём

listDays = ['Monday', 'Tuesday', 'Wedneday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
n = int(input('Input year day from 1 to 365\n'))
a = n % 7
if a < 6:
    print('No weekend day yet', '\n', a, '\n', listDays[a-1])
else:
    print('Hola, weekend day now')
