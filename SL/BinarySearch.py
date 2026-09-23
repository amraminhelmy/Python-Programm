SortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
min = 0
max = len(SortedArray) - 1
found = False
while min <= max and not found:
    mid = (min + max) // 2
    if SortedArray[mid] == target:
        print("Found at index:", mid)
        found = True
    elif SortedArray[mid] < target:
        min = mid + 1
    else:
        max = mid - 1

if not found:
    print("Not found in the list.")
