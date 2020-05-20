def sum(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIndex = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIndex]:
            maxSumIndex = i
    return [sums[maxSumIndex], buildSeq(array, sequences, maxSumIndex)]


def buildSeq(array, sequences, currentIndex):
    sequence = []
    while currentIndex is not None:

        sequence.append(array[currentIndex])
        currentIndex = sequences[currentIndex]
    return list(reversed(sequence))


print(sum([8,12, 2, 3, 15, 5, 7]))



