def maxDist(arr):
    n = len(arr)
    mp = dict()
    maxdist = 0

    for i in range(n):

        if arr[i] not in mp.keys():
            mp[arr[i]] = i

        else:
            maxdist = max(maxdist, i - mp[arr[i]])
    return maxdist


# driver
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
print(maxDist(arr))
