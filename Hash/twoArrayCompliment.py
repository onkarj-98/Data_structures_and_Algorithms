def compliment(array1, array2):

    result = []
    seen = set()
    for i in array2:
        seen.add(i)
    for j in array1:
        if seen.__contains__(j):
            continue
        else:
            result.append(j)
    return result


a = [1, 2, 3, 4, 5, 10]
b = [2, 3, 1, 0, 5]
print(compliment(a, b))

