class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def buildTree(levelorder, inorder):
    if inorder:
        for i in range(0, len(levelorder)):
            if levelorder[i] in inorder:
                node = Node(levelorder[i])

                io_index = inorder.index(levelorder[i])
                break
        if not inorder:
            return node
        node.left = buildTree(levelorder, inorder[0:io_index])
        node.right = buildTree(levelorder, inorder[io_index + 1:len(inorder)])
        return node


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)


levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]

root = buildTree(levelorder, inorder)

print("Iorder traversal of tree is:")
printInorder(root)
