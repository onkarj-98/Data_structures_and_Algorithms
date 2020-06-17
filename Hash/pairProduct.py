def product(array, x):
    seen = set()
    for i in array:
        seen.add(i)

    for j in array:
        num = x / j
        if seen.__contains__(num):
            return True
    return False


array = [-10, 20, 9, -4]
print(product(array, 400))
