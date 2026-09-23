x=(int(input("Input a number")))

while x < 11 :
    print("x is less than 10")
    x = int(input("Input a number"))

Students = ["Alice", "bob", "James", "alice", "bob"]
print(len(Students))
i = 0
found = False
while i < len(Students) and not found:
    if Students[i] == "bob":
        print("found in location " + str(i))
        found = True
    i += 1
