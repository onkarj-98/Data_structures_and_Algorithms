# Find whether an array is subset of another array
def isSubset(array1, array2):
    seen = set()
    flag = True
    # traverse first array
    for i in array1:
        seen.add(i)
    # search elements of second array in hash
    for j in array2:
        if seen.__contains__(j):
            continue
        else:
            flag = False
    return flag


# driver functions

array1 = [11, 1, 13, 21, 3, 7]
array2 = [11,3,7,1]

print(isSubset(array1,array2))
