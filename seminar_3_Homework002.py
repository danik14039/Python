'''Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
1 2 3 4 5
6
-> 5 '''
from random import randint
N = int(input('Введите количество элементов в списке: '))

X = int(input('Введите число Х: '))
some_list = []
found = 0
for i in range(N):
    some_list.append(randint(0, 10))
    if abs(some_list[i]-X)<abs(found - X):
        found = some_list[i]
print(some_list)
print(found)