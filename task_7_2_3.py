"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randrange
import statistics
from timeit import timeit


def func_median(data):
    return statistics.median(data)


num = [10, 100, 1000]
for item in num:
    rand_list = [randrange(0, 100) for _ in range(2 * item + 1)]
    # print(f'median = {func_median(rand_list)}')
    print(f'# func_median_{item}', timeit('func_median(rand_list)', globals=globals(), number=1000), 'sec')

# gnome_sort_median_10 0.0015565000066999346 sec
# gnome_sort_median_100 0.01587370000197552 sec
# gnome_sort_median_1000 0.3284515000123065 sec

# free_sorted_10 0.0206385999917984 sec
# free_sorted_100 0.41604569999617524 sec
# free_sorted_1000 3.352280699997209 sec

# func_median_10 0.0004958999925293028 sec
# func_median_100 0.00440330000128597 sec
# func_median_1000 0.14267189998645335 sec

'''
метод statistics.median эффективнее
'''
