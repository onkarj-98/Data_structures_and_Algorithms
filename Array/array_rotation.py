def leftRotate(arr,n,d):
    for _ in range(d):
        leftRotateByOne(arr,n)

def leftRotateByOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr,n):
    for i in range(n):
        print("%d"% arr[i],end = " ")


#driver program
arr = [1,2,3,4,5,6,7]
n = len(arr)
leftRotate(arr,n,2)
printArray(arr,n)
