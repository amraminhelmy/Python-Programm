fileData = ["Today is a lovely day \n I may go out and eat an ice cream \n or go to the park"]
data = ""
with open ("Text.txt", "w") as file1:
    file1.writelines(fileData)
    file1.close()
with open ("Text.txt", "a") as file1:
    file1.writelines("update it began to rain")
    file1.close()

with open ("Text.txt", "r+") as file1:
    data = file1.read()
    file1.close()

print (data)
