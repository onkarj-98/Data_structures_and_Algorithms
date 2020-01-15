class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insertLevelOrder(array, root, i, n):
    if i < n:
        root = Node(array[i])

        root.left = insertLevelOrder(array, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(array, root.right, 2 * i + 2, n)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(array)
    root = None
    root = insertLevelOrder(array, root, 0, n)
    inorder(root)
