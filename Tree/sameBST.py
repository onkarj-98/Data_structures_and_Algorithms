# time O(N^2) | space O(N^2)

def sameBST(array1, array2):
    if len(array1) != len(array2):
        return False

    if len(array1) == 0 and len(array2) == 0:
        return True

    if array1[0] != array2[0]:
        return False

    leftArray1 = getSmaller(array1)
    leftArray2 = getSmaller(array2)
    rightArray1 = getBigger(array1)
    rightArray2 = getBigger(array2)

    return sameBST(leftArray1, leftArray2) and sameBST(rightArray1, rightArray2)


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            smaller.append(array[i])


def getBigger(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger
