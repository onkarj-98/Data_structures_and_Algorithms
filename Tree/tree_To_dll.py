class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class List:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def convert(root, head=None):
    if root is None:
        return
    levelArray = levelOrder(root)
    for i in levelArray:
        new_node = List(i)
        if head is None:
            head = new_node
            new_node.prev = head
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    return head


def printList(head):
    if head is None:
        return

    current = head
    while current is not None:
        print(current.data)
        current = current.next


def levelOrder(root):
    levelArray = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        levelArray.append(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return levelArray


root = Tree(10)
root.left = Tree(12)
root.right = Tree(15)
root.left.left = Tree(25)
root.left.right = Tree(30)
root.right.left = Tree(36)
head = List(0)
head = convert(root)
printList(head)


