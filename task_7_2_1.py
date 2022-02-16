"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randrange
from timeit import timeit


def gnome_sort_median(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data[round(size / 2)]


num = [10, 100, 1000]
for item in num:
    rand_list = [randrange(0, 100) for _ in range(2 * item + 1)]
    # print(f'median = {gnome_sort_median(rand_list)}')
    print(f'# gnome_sort_median_{item}', timeit('gnome_sort_median(rand_list)', globals=globals(), number=1000), 'sec')
