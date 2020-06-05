# O(N^2) time | O(N) space
# def minNumberOfJumps(array):
#     jumps = [float("inf") for x in array]
#     jumps[0] = 0
#     for i in range(1, len(array)):
#         for j in range(0, 1):
#             if array[j] + j >= i:
#                 jumps[i] = min(jumps[j] + 1, jumps[i])
#     return jumps[-1]
#

# O(N) time | O(1) space

def minNumberOfJumps2(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i

    return jumps + 1


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps2(array))
