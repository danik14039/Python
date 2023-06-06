'''Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''
import random

n = int(input('Enter quantity of elements: '))
a = int(input('Enter first element: '))
d = int(input('Enter difference: '))

a_progression = [a+i*d if d!=0 else a for i in range(n+1)]
print(a_progression)

'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

a_list = [random.randint(-10, 25) for _ in range (0, 26)]
print(a_list)
print()
a = int(input('Enter 1st element of the range: '))
b = int(input('Enter 2-nd element of the range: '))
b_list = [i for i in range(len(a_list)) if a<=a_list[i]<=b]
print(b_list)