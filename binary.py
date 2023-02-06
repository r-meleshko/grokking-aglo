def binary_search(arr, low, high, x):
    if high >= low:  # Base condition, if active search has not finished

        mid = (high + low) // 2

        if arr[mid] == x:  # Success condition, return index
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1  # Error code if search has finished without result



arr = list(range(0, 1000))
print(binary_search(arr, 0, len(arr) - 1, 1002))