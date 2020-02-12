class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def builtTreeUtil(pre, preM, preIndex, l, h, size):
    if preIndex >= size or l > h: #base condition
        return None, preIndex
    root = Node(pre[preIndex])
    preIndex += 1
    if l == h:
        return root,preIndex
    i = 0
    for i in range(l, h + 1):  # we are finding pivot in preM
        if pre[preIndex] == preM[i]:
            break

    if i <= h:
        root.left, preIndex = builtTreeUtil(pre, preM, preIndex, i, h, size)
        root.right, preIndex = builtTreeUtil(pre, preM, preIndex, l + 1, i - 1, size)

    return root, preIndex


def builtTree(root, pre, preM, size):
    preIndex = 0
    root, x = builtTreeUtil(pre, preM, preIndex, 0,size-1,  size)
    inorder(root)


if __name__ == "__main__":
    pre = [1, 2, 4, 5, 3, 6, 7]
    preM = [1, 3, 7, 6, 2, 5, 4]
    root = Node(0)
    size = 7
    builtTree(root, pre, preM, size)
