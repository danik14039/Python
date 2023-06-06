''' Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes '''

def prime_number(n, i=2):
    if n == 1 or n == 2:
        return True
    elif n % i == 0:
        return False
    elif i*i>n:
        return True    
    return prime_number(n, i+1)

print(prime_number(101))
        






'''
Задача №37.

Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3 '''

def rev(array):
    if not array:
        return []
    return [array[-1]]+rev(array[:-1])

array = [1, 2, 3, 4, 5]

print(array)

print(rev(array))


def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'


n = int(input())
print(f(n))