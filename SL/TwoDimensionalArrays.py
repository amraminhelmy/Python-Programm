temperature =[
    [21,23,24,22,23,24,29],
    [22,20,19,28,28,17,20],
    [24,28,29,31,32,31,33],
    [23,25,21,26,22,20,19]]

print(temperature)

temperature[0][0] = 20
print(temperature)

temperature[2].append(30)
print(temperature)

##

count = 0
average = 0
for rows in temperature:
    print ("")
    for columns in rows:
        print(columns, end = " ")
        count = count + 1
        average = average + columns
    
print ("The average temperature is" + str(average/count))