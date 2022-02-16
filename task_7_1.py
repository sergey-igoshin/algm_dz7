"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randrange
from timeit import timeit


def sort_descending(data):
    n = 0
    while n < len(data) - 1:
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    return data


def sort_descending_flag(data):
    n = 0
    while n < len(data) - 1:
        flag = True
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                flag = False
        if flag:
            return data
        n += 1


rand_list = [randrange(-100, 100) for _ in range(10)]
rand_list2 = rand_list.copy()
print(rand_list)
print(sort_descending(rand_list))
print()
print(rand_list2)
print(sort_descending_flag(rand_list2))

print('# sort_descending', timeit('sort_descending(rand_list)', globals=globals(), number=10000), 'sec')
print('# sort_descending_flag', timeit('sort_descending_flag(rand_list2)', globals=globals(), number=10000), 'sec')

# sort_descending 0.04989749999367632 sec
# sort_descending_flag 0.005958199995802715 sec

'''
Флаг помогает сократить кол-во итераций, если список отсортированный, то сразу завершение
'''
