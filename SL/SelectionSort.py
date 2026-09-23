Students1 = ["smith", "bob", "James", "jack", "alice"]

for i in range(0, len(Students1)-1):
    key = i
    for j in range(i + 1, len(Students1)):
        if (Students1[j]<Students1[key]):
            key = j
    temp = Students1[key]
    Students1[key] = Students1[i]
    Students1[i] = temp
print(Students1)