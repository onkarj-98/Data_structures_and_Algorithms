def TwoArraySum(array1, array2, targetSum):
    nums = set()
    for num in array1:
        potentialMatch = targetSum - num
        nums.add(potentialMatch)
    for num1 in array2:
        if nums.__contains__(num1):
            return True
        else:
            False


array1 = [0,0,-5,30,212]
array2 = [-10,20,-3,9]

print(TwoArraySum(array1,array2,targetSum=-8))