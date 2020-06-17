from _collections import deque


def stockspan(price):
    if price is None:
        return
    span = []
    stack = deque()
    for i in range(len(price) - 1):
        while len(stack) > 0 and price[i] > stack[len(stack) - 1]:
            stack.pop()
        if len(stack) == 0:
            span[i] = i + 1
        else:
            span[i] = i - stack[len(stack) - 1]
        stack.append(i)
    return span


price = [100, 80, 60, 70, 60, 75, 85]
stockspan(price)
