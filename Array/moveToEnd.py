def move(array, toMove):
    start = 0
    end = len(array) - 1
    while start < end: # breaking the loop
        while array[end] == toMove:
            end -= 1
        if array[start] == toMove:
            array[start],array[end] = array[end] , array[start]
        start += 1 # if start is not equal to toMove
    return array


