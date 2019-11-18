'''Find the height of binary tree (Iterative Way)'''
class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
def heightOfTree(root):
    if root is None:
        return 0

    q = [] # initialize the queue
    q.append(root) # append the root to queue
    height = 0
    while True:
        nodeCount = len(q)
        if nodeCount == 0:
            return height
        height += 1

        while(nodeCount > 0):
            node = q[0]
            q.pop(0)
            if node.right is not None:
                q.append(node.right)
            if node.left is not None:
                q.append(node.left)
            nodeCount -= 1


root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(9)
root.left.left.left = Node(7)
root.left.left.left.left = Node(10)
print(heightOfTree(root))

