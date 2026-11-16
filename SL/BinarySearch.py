SortedArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
target = 'e'


def find(item, list):
    min = 0
    max = len(list) - 1
    found = False
     
    while min <= max and not found:
        mid = (min + max) // 2
        if list[mid] == item:
            print("Found at index:", mid)
            found = True
        elif list[mid] < item:
            min = mid + 1
        else:
            max = mid - 1
    if not found:
        print("Not found in the list.")

find(target, SortedArray)
