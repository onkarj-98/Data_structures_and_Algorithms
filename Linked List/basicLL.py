# i ll be writting code for basic implementation of
# single list , you can apply this basic structure for solving LL problems

class Node:
    def __init__(self, data):  # initialization of class , it takes data as parameter
        self.data = data
        self.next = None  # definig a structure of list


class List:
    def __init__(self):  # initialization
        self.head = None  # reset the head = None when new list is created

    def insert(self, data):
        new_node = Node(data)
        # i.e. we are adding first element into the list
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


def main():  # this is a main function
    A = List()  # 'A' is new object of our List class i.e it is a new Linked list
    A.insert(10)  # Apply any functions on list that you created
    A.insert(12)
    A.insert(13)
    A.insert(15)
    A.printList()


if __name__ == '__main__':
    main()

# This is basic structure , you can use in any programming interview.
