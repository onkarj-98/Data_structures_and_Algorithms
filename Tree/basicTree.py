class Node:  # This is Node structure
    def __init__(self, data):
        self.data = data  # we store the data in data field
        self.right = None  # right nodes address ? you can say that
        self.left = None  # left node address


def insert(root, data):  # This is recursive version
    if root is None:  # checks for the root is empty or not
        new_node = Node(data)  # creats the new node
        return new_node  # return new node
    elif data < root.data:  #
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def inorder(root):  # inorder traversal
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':  # main
    root = None
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 9)
    root = insert(root, 10)
    root = insert(root, 14)
    inorder(root)
    # This is basic structure , you can use in any programming interview.
