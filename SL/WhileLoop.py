#x=(int(input("Input a number")))
#
#while x < 11 :
 #   print("x is 10 or less than 10")
   # x = int(input("Input a number"))

Students = ["edo", "Alice", "bob", "James", "alice", "bob"]
name = input("Input a name to search for")

def LinearSearch (target,list):
    i = 0
    found = False #which means not found yet
    while i < len(list) and found == False:
        if list[i] == target:
            print("found in location " + str(i))
            found = True
        i = i + 1

    if not found:
        print(target + " not found")

print(LinearSearch(name,Students))
