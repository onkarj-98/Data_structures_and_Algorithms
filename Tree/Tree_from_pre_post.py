class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def buildTree(preorder, postorder, postStart, postEnd):
    if postStart > postEnd:
        return
    node = Node(preorder[buildTree.preIndex])
    buildTree.preIndex += 1
    if postStart == postEnd:
        return node
    postIndex = Search(postorder, postStart, postEnd, preorder[buildTree.preIndex + 1])

    node.left = buildTree(preorder, postorder, postStart, postIndex - 1)
    node.right = buildTree(preorder, postorder, postIndex + 1, postEnd - 1)
    return node


def Search(array, postStart, postEnd, data):
    for i in range(postStart, postEnd + 1, data):
        if array[i] == data:
            return i


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
n = len(post)
buildTree.preIndex = 0
root = buildTree(pre, post, 0, n-1)
print("Inorder traversal of built tree")
inorder(root)
