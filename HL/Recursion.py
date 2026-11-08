def natural(num):
    if (num <= 1):
        return 1
    else:
        return num + natural(num - 1) #Function calls itself, this is recursion
print(natural(10))


def fibonacci(num):
    if (num == 0) or (num == 1):
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2) #Function calls itself, this is recursion
print (fibonacci(10))