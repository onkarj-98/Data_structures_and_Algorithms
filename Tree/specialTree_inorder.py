class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def buildTree(inorder, start, end):
    if start > end: # termination case
        return None
    i = findMax(inorder, start, end)

    root = Node(inorder[i])

    if start == end: # base case
        return root
    root.left = buildTree(inorder, start, i - 1) # isolate the root node
    root.right = buildTree(inorder, i + 1, end)

    return root


def findMax(array, start, end):
    i, Max = 0, array[start]
    maxind = start
    for i in range(start + 1, end + 1):
        if array[i] > Max:
            Max = array[i]
            maxind = i
    return maxind


if __name__ == '__main__':
    inorder = [5, 10, 40, 30, 28]
    l = len(inorder)

    root = buildTree(inorder,0,l-1)
