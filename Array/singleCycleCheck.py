# time o(N) | space O(1)
def check(array):
    n = len(array)
    numElementedVisited = 0
    currentIndex = 0
    while numElementedVisited < n:
        if numElementedVisited > 0 and currentIndex == 0:
            return False
        numElementedVisited += 1
        currentIndex = getNextIndex(currentIndex, array)

    if currentIndex == 0:
        return True


def getNextIndex(currentIndex, array):
    jump = array[currentIndex]
    nextIndex = (currentIndex + jump) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)


array = [2, 3, 1, -4, -4, 2]
print(check(array))