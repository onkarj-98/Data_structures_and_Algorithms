class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def reverse_levelOrder(root):
    if root is None:
        return
    queue = []
    stack =[]
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        stack.append(node)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    while len(stack) > 0:
        node = stack.pop()
        print(node.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
reverse_levelOrder(root)