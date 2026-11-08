def binary_search(sorted_array, target):
    min_index = 0
    max_index = len(sorted_array) - 1
    found = False

    while min_index <= max_index and not found:
        mid_index = (min_index + max_index) // 2
        if sorted_array[mid_index] == target:
            return mid_index
            found = True
        elif sorted_array[mid_index] < target:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1

    if not found:
        return -1  # Return -1 to indicate the target is not found

SortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(SortedArray, 5)
print("Index of target:", result)
