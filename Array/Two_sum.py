"""


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



"""

""" Two Number Sum in Array """
""" O(n^2) time and O(1) space"""


def twoNumberSum(array, targetSum):  # it is double for loop method
    for i in range(len(array) - 1):  # we select first element in this loop
        first_num = array[i]
        for j in range(i + 1, len(array)):  # then we compare this to all elements in loop as second
            second_num = array[j]  # element here
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []


""" Using hash table"""
""" O(n) time and O(n) space"""


def twoNumberSumHash(arr, targetSum):  # Hash Table method
    nums = {}  # empty dict in python
    for num in arr:  # first we scan the array
        potentialMatch = targetSum - num  # then we check for potential match
        if potentialMatch in nums:  # if potential match in hashTable
            return [potentialMatch, num]  # return the match
        else:
            nums[num]  # Add that number in hashTable
    return []  # return just list


""" Actually its like x + y = targetSum ie y = tagetsum - x and you have to look up for y in hashtable"""

"""Using Two pointers method 
O(n long) time and O(1) space
"""


def twoNumSumPointer(arr, targetSum):  # Two pointer method
    arr.sort()  # step 1
    left = 0
    right = len(arr) - 1  # step 2
    while left < right:  # we don't want to left exceed than right
        currentSum = arr[left] + arr[right]  # step 3
        if currentSum == targetSum:
            return [arr[left], arr[right]]
        elif currentSum < targetSum:  # step 4
            left += 1
        elif currentSum > targetSum:  # step 5
            right += 1
    return []


""" Its actually efficient method but it requires array in sorted manner,
step 1 : sort the array
step 2 : assign left and right pointer
step 3 : calculate sum ( currrentSum )
        check if currentSum is equal to targetSum if yes then return.
step 4 : if currentSum is less than target sum 
         we have to increase left pointer because we need sum as close to the target sum
        ie current sum is low we need higher value than current
step 5: if currentSum is higher than target sum
        we have to decrease the right pointer 
        because as array is sorted so higher value's at to be right ,
        so current value is higher than the targetSum so, we want to reduce the sum as close to target sum 
"""
"""You can give 3 approaches to interviewer and discuss about their trade off's between space and time"""

