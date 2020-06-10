"""Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
Размер списка n ввести с клавиатуры. Удалить элементы, индексы которых кратны 3."""
import random
n=int(input("Введите размер списка:\n"))
A=[]
for i in range(n):
    a = random.randint(0,99)
    A.append(a)

print("Список: ", end =' ')
for i in range(n):
    print(A[i], end = ' ')

i = len(A)-1
while i >= 0:
    if i % 3 == 0:
        del A[i]
    i += -1

print("\nСписок2: ", end =' ')
for i in range(len(A)):
    print(A[i], end = ' ')

