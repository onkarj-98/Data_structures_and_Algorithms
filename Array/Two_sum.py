""" Two Number Sum in Array """
""" O(n^2) time and O(1)"""


def twoNumberSum(array, targetSum):  # it is double for loop method
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []


""" Using hash table"""
""" O(n) time and O(n) space"""


def twoNumberSumHash(arr, targetSum):  # Hash Table method
    nums = {}
    for num in arr:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


"""Using Two pointers method 
O(n long) time and O(1) space
"""


def twoNumSumPointer(arr, targetSum):  # Two pointer method
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return [arr[left], arr[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right += 1
    return []
