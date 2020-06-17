class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def diagonalUtil(root, d, diagonalMap):
    if root is None:
        return

    try:
        diagonalMap[d].append(root.data)
    except:
        diagonalMap[d] = root.data

    diagonalUtil(root.left, d + 1, diagonalMap)
    diagonalUtil(root.right, d, diagonalMap)


def diagonalPrint(root, k):
    if root is None:
        return
    diagonalMap = dict()
    diagonalUtil(root, 0, diagonalMap)
    for i in diagonalMap:
        for j in diagonalMap[i]:
            k -= 1
            if k == 1:
                print(j)


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left =Node(4)
root.left.right.right =Node(7)

diagonalPrint(root, k= 9)



