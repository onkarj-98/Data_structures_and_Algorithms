class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalUtil(root, d, diagonalMap):
    # base Case
    if root is None:
        return

    try:
        diagonalMap[d].append(root.data)
    except KeyError:
        diagonalMap[d] = [root.data]

    diagonalUtil(root.left, d + 1, diagonalMap)
    diagonalUtil(root.right, d, diagonalMap)


def diagonalPrint(root):
    diagonalMap = dict()
    diagonalUtil(root, 0, diagonalMap)
    print("Diagonal traversal ")
    for i in diagonalMap:
        for j in diagonalMap[i]:
            print(j)
        print(" ")


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonalPrint(root)