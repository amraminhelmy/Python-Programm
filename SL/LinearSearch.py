Students1 = ("smith", "bob", "James", "jack", "alice")
target = "James"
found = False
for i in range(len(Students1)):
    if Students1[i] == target:
        found = True
        print("Found " + target + " at index " + str(i))
        break

if not found:
    print(target + " not found in the list.")