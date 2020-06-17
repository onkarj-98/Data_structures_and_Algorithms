class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIndex = (len(array)- 2) // 2
        for currentIndex in reversed(range(firstParentIndex)):
            self.siftDown(currentIndex, len(array)- 1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex: # check if child one exist
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1 # check if child two
            # present other wise -1
            if childTwoIndex != 1 and heap[childTwoIndex] < heap[childOneIndex]: # compa
                # re between child one and child two
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex

            if heap[indexToSwap] < heap[currentIndex]: # compare for smaller elements
                self.swap(currentIndex, indexToSwap, heap)
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 2
            else:
                break

    def siftUp(self, currentIndex, heap):
        parentIndex = (currentIndex - 1) // 2 # obtain parent index first
        while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]: # compare with current and parent
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex # assign resp indexes
            parentIndex = (currentIndex - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap) # swap with first element in array
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

