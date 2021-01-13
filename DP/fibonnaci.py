
def fibonacci(n, mem = {}):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    else:
        mem[n] = fibonacci(n - 1, mem) + fibonacci(n - 2, mem)
        return mem[n]


print(fibonacci(12))

