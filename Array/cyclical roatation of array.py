def rightRotatebyOne(arr):
    n = len(n)
    temp = arr[0]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp





def printArray(arr):
    n = len(arr)
    for i in range(n):
        print("%d"%arr[i],end = " ")
#driver code

arr = [1,2,3,4,5]
rightRotatebyOne(arr)
printArray(arr)
