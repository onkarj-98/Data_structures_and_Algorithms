class Node:
     def __init__(self,data): # binary tree structure
         self.data = data
         self.right = None
         self.left = None
def lca(root,n1,n2):
    if root is None: #if root is None return None
        return None
    if root.data is n1 or root.data is n2: # we check for each node in tree
        return root
    left_lca = lca(root.left,n1,n2) # otherwise we just iterate through left subtree
    right_lca = lca(root.right,n1,n2) # same for right sub tree

    if left_lca is not None and right_lca is not None: # if left and right subtree return root then its lca
        return root
    if left_lca is None and right_lca is None: # oops not found!
        return None
    if left_lca is not None: # if left lca is not null and  right is the return left lca
        return left_lca
    else:
        return right_lca    # if left is null and right not null then return left lca

root = Node(3)
root.left = Node(6)
root.left.left = Node(2)
root.left.right = Node(11)
root.left.right.left = Node(9)
root.left.right.right = Node(5)
root.right = Node(8)
root.right.right=Node(13)
root.right.right.left= Node(7)
print(lca(root,9,5).data)