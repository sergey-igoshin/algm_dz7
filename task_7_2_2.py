"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randrange
from timeit import timeit


def free_sorted(data):
    for i in range(len(data)):
        a = b = c = 0
        for j in range(len(data)):
            if data[i] < data[j]:
                a += 1
            elif data[i] > data[j]:
                c += 1
            else:
                b += 1
        b -= 1
        if a == c or a == b + c or c == a + b or (b > 1 and abs(c - a) < b):
            return data[i]


num = [10, 100, 1000]
for item in num:
    rand_list = [randrange(0, 100) for _ in range(2 * item + 1)]
    # print(f'median = {free_sorted(rand_list)}')
    print(f'# free_sorted_{item}', timeit('free_sorted(rand_list)', globals=globals(), number=1000), 'sec')
