def isDuplicate(array, k):
    n = len(array)
    mp = set()
    flag = True
    counter = -1

    for i in array:
        counter += 1
        if mp.__contains__(i):
            if k >= counter:
                flag = False
                return flag
        else:
            mp.add(i)
    return flag


# driver
array = [1, 2, 3, 1, 4, 5]
k = 3
print(isDuplicate(array, k))
