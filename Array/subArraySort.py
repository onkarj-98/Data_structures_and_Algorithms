def sort(array):
    minOutofOrder = float("inf")
    maxOutOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutofOrder(i, num, array):
            minOutofOrder = min(minOutofOrder, num)
            maxOutOrder = max(maxOutOrder, num)
    if minOutofOrder == float("inf"):
        return [-1, 1]
    leftIndex = 0
    while minOutofOrder >= array[leftIndex]:
        leftIndex += 1
    rightIndex = len(array) - 1
    while maxOutOrder <= array[rightIndex]:
        rightIndex -= 1
    return [leftIndex, rightIndex]


def isOutofOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i+ 1] or num < array[i- 1]
