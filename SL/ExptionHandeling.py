Students = ["Alice", "bob", "James", "alice", "bob"]
try:
    print(Students[5]) #This will raise an IndexError because the index 5 is out of range for the list Students, which has indices 0 to 4.
except:
    print ("An error has occurred")
finally:
    print ("The program has ended safely")


try:
    print(Students[4]) #This will not raise an error because the index 4 is valid for the list Students, which has indices 0 to 4. It will print "bob".
except:
    print ("An error has occurred")
finally:
    print ("The program has ended safely")