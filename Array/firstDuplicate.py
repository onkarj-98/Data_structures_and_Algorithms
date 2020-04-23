def firstDuplicate(array): #Hash set method
    seen = set()      # O(n) | space of array

    for i in array:
        if seen.__contains__(i):
            return i
        else:
            seen.add(i)
    return -1


array = [1, 2, 1, 2, 3, 3, ]
print(firstDuplicate(array))

