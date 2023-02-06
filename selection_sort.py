def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        smallest_index = find_smallest(array)
        sorted_array.append(array.pop(smallest_index))
    return sorted_array
