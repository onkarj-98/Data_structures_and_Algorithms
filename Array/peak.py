def isPeak(array):
    potentialPeak = [array[0], 0]

    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            if array[i] > potentialPeak[0]:
                potentialPeak = [array[i], i]

    if array[len(array) - 1] > potentialPeak[0]:
        potentialPeak = [array[len(array) - 1],len(array)]

    return potentialPeak[1]


array = [60, 2, 27, 3, 4, 0, 0, 6, 5, -1, -3, 2, 0]
print(isPeak(array))

array = [1, 3, 2]
print(isPeak(array))

array = [5, 4, 3, 2, 1, 2, 1]
print(isPeak(array))

