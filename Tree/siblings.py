class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def check(root,n1,n2):
    if root is None:
        return
    if(root.left and root.right):
        left = root.left.data
        right = root.right.data
        if left == n1 and right == n2:
            return True
        elif left == n2 and right == n1:
            return True

    if root.left:
        check(root.left,n1,n2)
    if root.right:
        check(root.right,n1,n2)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)

print(check(root,6,7))
