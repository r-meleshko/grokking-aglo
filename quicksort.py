def sum(arr):
    if len(arr) == 2:
        return arr[0] + arr[1]
    return arr[0] + sum(arr[1:])


def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


def get_max(arr, max):
    if len(arr) == 1:
        return max if max > arr[0] else arr[0]
    else:
        max = max if max > arr[1] else arr[1]
        return get_max(arr[1:], max)


def get_max_2(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    submax = get_max_2(arr[1])
    return arr[0] if arr[0] > submax else arr[1]

import random

arr = [random.randint(1, 100) for x in range(7)]


print(arr)
print(get_max(arr, arr[0]))