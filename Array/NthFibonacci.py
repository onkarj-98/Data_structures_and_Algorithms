# we are going to use memoization due to stack exlposion
def getNthFib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


# In this solution it runs O(2^n) times

# Using    memoization
# In this method we reduce the repetitive calculations
def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]


# iterative

def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]