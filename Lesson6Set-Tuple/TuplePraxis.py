# Написать программу для конвертации кортежа в string
ab = (3.4, 56, "Some", "Hi", 7)
abc = str(ab)
print(abc)
print('\n')

# 2 Написать программу, которая находит длину кортежа
tup = (3.4, 56, "Some", "Hi", 7, 3.8, 44)
print(len(tup))

# 3.1 Вывести лишь третий элемент с конца
print(tup[3])

# 3.2 каждый второй элемент кортежа, начиная с третьего.


# 4 Сконвертируйте из списка в кортеж
numList = [213, 43, 5, 6, 86]
numList2 = tuple(numList)
print(numList2)

# 5 Создайте кортеж состоящий из:2 чисел строки числа с точкой
numbers = (5, 7, 'wolf', 5.7)
k = 0
while k < len(numbers):
    print(numbers[k])
    k += 1


