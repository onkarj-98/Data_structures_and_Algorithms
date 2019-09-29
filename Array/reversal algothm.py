#reversal algorithm for rotating array by factor
#time complexity is O(n)
def reverse(arr,start,end):
    while start < end :
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end = end -1

def leftRotate(arr,d):
    if d == 0:
        return
    n = len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

def printArray(arr,n):
    for _ in range(n):
        print("%d"%arr[_],end=" ")

#driver code

arr = [1,2,3,4,5,6,7,8]
n = len(arr)
leftRotate(arr,3)
printArray(arr,n)


