# O(N^2) time | O(1) space
def longestPalindrome(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd_palindrome = getLongestPalindrome(string, i - 1, i + 1)
        even_palindrome = getLongestPalindrome(string, i - 1, i)
        longest = max(odd_palindrome, even_palindrome, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]


def getLongestPalindrome(string, leftIndex, rightIndex):
    while leftIndex >= 0 and rightIndex < len(string):
        if string[leftIndex] != string[rightIndex]:
            break
        leftIndex -= 1
        rightIndex += 1
    return [leftIndex + 1, rightIndex]
