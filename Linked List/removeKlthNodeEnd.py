class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next= self.head
            self.head = new_node

    def deleteKth(self, k):
        if self.head is None:
            return
        prev=first = second = self.head
        counter = 1
        while counter != k:
            second = second.next
            counter += 1
        while second.next is not None:
            prev = first
            first = first.next
            second = second.next
        prev.next = first.next
        del first

    def printList(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            print(current.data)

            current = current.next


list = List()
list.insert(10)
list.insert(12)
list.insert(14)
list.insert(16)
list.insert(18)
list.insert(20)
list.insert(22)
list.printList()
print("\n")
list.deleteKth(3)
list.printList()





