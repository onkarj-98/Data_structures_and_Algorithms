def kadane(array):
    maxEndingHere = array[0]  # sum of previous elements in array
    maxSoFar = array[0]       # global max value
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxEndingHere,maxSoFar)
    return maxSoFar


# time complexity is O(n)
# space complexity is O(1)
# This is kadane's algorithm for max sum in array






