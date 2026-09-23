Students1 = ["smith", "bob", "James", "jack", "alice"]
Swapping = False
for i in range(0,len(Students1)-1):
    for j in range(0, len(Students1)-1-i):
        if Students1[j] > Students1[j+1]:
            temp = Students1[j]
            Students1[j] = Students1[j+1]
            Students1[j+1] = temp
            Swapping = True
    if not Swapping:
        break
print("Sorted Students1:", Students1)


            

    