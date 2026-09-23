Students = ("John", "Alice", "Bob")

if len(Students) <= 1:
    print(Students)
else:
    pivot = Students[0]
    less = [x for x in Students[1:] if x <= pivot]
    greater = [x for x in Students[1:] if x > pivot]
    print(Students(less) + [pivot] + Students(greater))


