# 1
def invert(root):
    queue = [root]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            return
        swap(current)
        queue.append(current.left)
        queue.append(current.right)


def swap(node):
    temp = node.right
    node.right = node.left
    node.left = temp


# 2

def invert(root):
    if root is None:
        return
    swap(root)
    invert(root.left)
    invert(root.right)


# 3

def invert(root):
    if root is None:
        return
    invert(root.left)
    invert(root.right)

    temp = root.right
    root.right = root.left
    root.left = temp
