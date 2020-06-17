import unittest


# First Missing Positive Integer
def firstPositive(array):
    smallestBeforeZero = array[0]
    secondSmallestBeforeZero = array[0]
    for i in array:
        if smallestBeforeZero >= i > :
            secondSmallestBeforeZero = smallestBeforeZero
            smallestBeforeZero = i
    missing = secondSmallestBeforeZero - smallestBeforeZero
    return missing


# class Test(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(firstPositive([3, 4, -1, 1]), 2, "Should be 2")
#
#     def test_2(self):
#         self.assertEqual(firstPositive([5, 4, 2, 1, -1, 8]), 3, "should be 3")
#
#
# if __name__ == '__main__':
#     unittest.main()

print(firstPositive(array=[3, 4, -1, 1]))
print(firstPositive(array=[5, 4, 2, 1, -1, 8]))