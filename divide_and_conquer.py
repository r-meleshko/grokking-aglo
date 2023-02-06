def get_sum(array):
    if len(array) == 1:
        return array[0]
    return array[0] + get_sum(array[1:])


def get_len(array):
    if len(array) == 1:
        return 1
    return 1 + get_len(array[1:])


def get_max(array, maximum):
    if len(array) == 0:
        return maximum
    else:
        if array[0] > maximum:
            return get_max(array[1:], array[0])
        else:
            return get_max(array[1:], maximum)


def better_get_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = arr[1:]
    return arr[0] if arr[0] > sub_max else sub_max


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less, greater = [], []
        for i in arr[1:]:
            greater.append(i) if i > pivot else less.append(i)
        return qsort(less) + [pivot] + qsort(greater)
