def findBMI(userWeight, userHeight):
    BMI = userWeight / (userHeight * userHeight)
    if BMI < 18.5:
        print("Your BMI is " + str(BMI) + " which means you are underweight")
    elif BMI >= 18.5 and BMI < 24.9:
        print("Your BMI is " + str(BMI) + " which means you are normal weight")
    elif BMI >= 25 and BMI < 29.9:
        print("Your BMI is " + str(BMI) + " which means you are overweight")
    

inputWeight = float(input("Enter your weight in kg: "))
inputHeight = float(input("Enter your height in meters: "))
findBMI(inputWeight, inputHeight)
