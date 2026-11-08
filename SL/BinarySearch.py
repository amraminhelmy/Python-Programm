SortedArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
target = 'e'
min = 0
max = len(SortedArray) - 1
print(len(SortedArray))
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
