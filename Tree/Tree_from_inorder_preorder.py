class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def buildTree(inOrder, preOrder, inStart, inEnd):
    if inStart > inEnd:
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStart == inEnd: #important case
        return tNode
    inIndex = Search(inOrder, inStart, inEnd, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, inStart, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return tNode


def Search(arr, start, end, data):
    for i in range(start, end + 1):
        if arr[i] == data:
            return i


def printLevel(root):
    if root is None:
        return
    else:
        queue = []
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].data),
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
print("Level Order Traversal of Tree is:")
printLevel(root)
print("Inorder traversal of Tree is:")
printInorder(root)
