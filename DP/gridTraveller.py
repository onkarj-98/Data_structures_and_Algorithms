def gridTraveller(m, n, memo = {}):
    key = (m ,n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key]  = gridTraveller(m - 1, n) + gridTraveller(m, n -1)
    return memo[key]



print(gridTraveller(12,10)) 
