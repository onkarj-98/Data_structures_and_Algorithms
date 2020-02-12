class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreeUtil(pre, preLN, preIndex, n):
    index = preIndex
    if index == n:
        return
    node = Node(pre[index])
    preIndex += 1

    if preLN[index] == 'N':
        node.left, preIndex = buildTreeUtil(pre, preLN, preIndex, n)
        node.right, preIndex = buildTreeUtil(pre, preLN, preIndex, n)
    return node, preIndex


def buildTree( pre, preLN, n):
    preIndex = 0
    root, x = buildTreeUtil(pre, preLN, preIndex, n)
    preorder(root)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


if __name__ == '__main__':
    pre = [10, 30, 20, 5, 15]
    preLN = ['N', 'N', 'L', 'L', 'L']
    n = len(pre)

    buildTree( pre, preLN, n)
