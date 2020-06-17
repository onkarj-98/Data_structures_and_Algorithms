class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def val(root):
    if root is None:
        return
    if root.left.data < root.data < root.right.data:
        return True


    val(root.left)
    val(root.right)


root = Node(10)
root.left = Node(9)
root.right = Node(15)
root.left.left = Node(12)

print(val(root))
