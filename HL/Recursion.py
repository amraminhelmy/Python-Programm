def natural (num):
    if (num <= 1):
        return 1
    else:
        return num + natural(num - 1)

print(natural(5))