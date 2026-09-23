Students1 = ("alice", "bob", "james", "alice", "bob", "james")
print(len(Students1))
for i in range(0,6):
    if Students1[i] == "bob":
        print("found in location " + str(i))
print(Students1)

##

Students2 = ["Alice", "bob", "james", "alice", "bob"]
count = 0
print(len(Students2))
for student in Students2:
    if student == "bob":
        print("found in location " + str(count))
    count += 1
Students2.append("bob")
Students2.remove("James")
print(Students2)


