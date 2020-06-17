class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getVerticalOrder(root, hd, m):
    if root is None:
        return

    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]

    getVerticalOrder(root.left, hd - 1, m)
    getVerticalOrder(root.right, hd + 1, m)


def printVerticalOrder(root):
    m = dict()

    hd = 0

    getVerticalOrder(root, hd, m)

    for index, values in enumerate(sorted(m)):  # Traverse the map and print nodes at every horizontal
        # distance (hd)
        for i in m[values]:
            print(i),


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print("Vertical order traversal is ")
printVerticalOrder(root)
