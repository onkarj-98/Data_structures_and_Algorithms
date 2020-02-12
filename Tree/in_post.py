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


def Search(array, instart, inend, data):
    i = 0
    for i in range(instart, inend + 1):
        if array[i] == data:
            break
    return i


def buildTree(ino, post, instart, inend):
    if instart == inend:
        return
    root = Node(post[buildTree.postIndex])

    buildTree.postIndex -= 1

    if instart == inend or buildTree:
        return root

    i = Search(ino, instart, inend, root.data)


    root.right = buildTree(ino,post,i+1,inend)
    root.left = buildTree(ino,post,instart,i-1)

    return root


if __name__ == '__main__':
    ino = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]

    size = len(post)
    inend = size
    instart = 0
    buildTree.postIndex = size - 1
    root = buildTree(ino,post,instart,inend)
    inorder(root)
