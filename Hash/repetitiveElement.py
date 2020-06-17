def findElement(array):
    seen = set()
    for i in array:
        if seen.__contains__(i):
            return i
        seen.add(i)

    return -1


arr = [9, 8, 2, 6, 1, 8, 5, 3]
print(findElement(arr))
