fileData = ["Today is a lovely day \n I may go out and eat an ice cream \n or go to the park"]
data = ""

with open("Text.txt", "w") as file1: #"W" is used to write to a file, if the file already exists, it will overwrite the existing content.
    file1.writelines(fileData)
    file1.close()

with open("Text.txt", "a") as file1: # "A" is used to append to a file, if the file already exists, it will add the new content to the end of the existing content.
    file1.writelines("update it began to rain")
    file1.close()

with open("Text.txt", "r+") as file1: # "R+" is used to read and write to a file, if the file already exists, it will overwrite the existing content.
    data = file1.read()
    file1.close()

print(data)
