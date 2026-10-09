Students = ["John", "Alice", "Bob"]

if len(Students) <= 1:
    print(Students)
else:
    pivot = Students[0]
    less = [x for x in Students[1:] if x <= pivot]
    greater = [x for x in Students[1:] if x > pivot]
    print(Students(less) + [pivot] + Students(greater))


def quickSort (start, finish, numbers):
    if (start==finish):
        return
    left = start
    right = finish
    pivot = numbers[int ((start+finish)/2)]
    print ("start: ", start, "finish: ", finish, "left: ", left, "right: ", right, "pivot: ", pivot)

    while left<right: 
        while numbers[left]<pivot:
            left = left + 1
            print ("left: ", left)
    while numbers [right] >pivot: 
            right = right - 1
            print ("right: ", right) 
    if left<=right: 
        temp = numbers[left] 
        numbers [left] = numbers[right] 
        numbers [right] = temp 
        left = left + 1 
        right = right - 1
        print ()
        for i in range (len(numbers)):
            print (numbers[i], " ", end="")
        print()
        print("left: ", left)

    print("right: ", right)
    print ("quickSort from start: ", start, " to right: ", right)
    print ("quickSort from left: ", left, " to finish: ", finish)

    quickSort (left, finish, numbers)


numbers = [16,13,4,6,22,1,9,5]
quickSort(0, len(numbers)-1, numbers)
for i in range(len(numbers)):
    print (numbers[i], " ", end="")



