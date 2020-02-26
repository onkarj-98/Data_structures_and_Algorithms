from collections import defaultdict


def findMinDeletion(array):
    n = len(array)
    max_freq = 0

    hash = defaultdict(lambda: 0)

    for i in range(n):
        hash[array[i]] += 1

    for i in hash:
        if max_freq < hash[i]:
            max_freq = hash[i]

    return n - max_freq


#  driver

array = [4, 3, 4, 4, 2, 4]
print(findMinDeletion(array))
