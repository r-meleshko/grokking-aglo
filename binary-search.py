
def binary_iter(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == item:
            return mid
        elif item > arr[mid]:
            low = mid + 1
        elif item < arr[mid]:
            high = mid - 1
    return None


def binary_recurs(arr, item, low, high):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == item:
            return mid
        elif item > arr[mid]:
            return binary_recurs(arr, item, mid + 1, high)
        elif item < arr[mid]:
            return binary_recurs(arr, item, low, mid - 1)
    else:
        return None


arr = [2, 3, 4, 10, 40, 41]

print(binary_recurs(arr, 4, 0, len(arr) - 1))