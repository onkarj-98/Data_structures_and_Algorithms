class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Time O(N)
# Space O(1)
def find_depth(root, target):
    if root is None:
        return 0
    depth = -1
    if root.data == target:
        return  depth + 1
    depth = find_depth(root.left, target)
    if depth >= 0:
        return depth + 1
    depth = find_depth(root.right, target)
    if depth >= 0:
        return depth + 1
    









if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(44)
    root.left.left = Node(223)
    root.right.right = Node(122)
    root.right.right.right = Node(231)
    root.right.right.right.right = Node(2323)

    print(find_depth(root, 44))

