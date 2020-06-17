class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def branchSum(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.data
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(9)
root.left.left.left = Node(8)
root.right.right = Node(7)
root.right.left = Node(6)

print(branchSum(root))
