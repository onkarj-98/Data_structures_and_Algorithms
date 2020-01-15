class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Conversion:
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def convertList(self):
        global rightChild
        queue = []
        if self.head is None:
            self.root = None
            return
        self.root = Node(self.head.data)
        queue.append(self.root)

        self.head = self.head.next  # one step
        while self.head:
            parent = queue.pop(0)

            leftChild = Node(self.head.data)
            queue.append(leftChild)
            self.head = self.head.next  # second step
            if self.head:
                rightChild = Node(self.head.data)
                queue.append(rightChild)
                self.head = self.head.next  # third step
            # assigning
            parent.left = leftChild
            parent.right = rightChild

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


conv = Conversion()
conv.push(10)
conv.push(12)
conv.push(13)
conv.push(15)
conv.push(66)
conv.push(77)
conv.push(64)
conv.push(88)
conv.convertList()
print("Inorder traversl of constructed binary tree is :")
conv.inorder(conv.root)
