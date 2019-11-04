class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def insert(root,data):
    if root is None:
        new_node = Node(data)
        return new_node
    elif data < root.data:
         root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)
    return root
def LCA(root,n1,n2):
    if root.data > max(n1,n2): # here we check if max of any of n1 and n2 , root.data is grater than maz(n1,n2) go to left
        return LCA(root.left,n1,n2)
    elif root.data < min(n1,n2): # here if min(n1,n2) if root.data is minimum than n
        return LCA(root.right,n1,n2)
    else:
        return root.data

if __name__ == '__main__':
    root = None
    root = insert(root,10)
    root = insert(root,-10)
    root = insert(root,30)
    root = insert(root,8)
    root = insert(root,25)
    root = insert(root,60)
    root = insert(root,6)
    root = insert(root,9)
    root = insert(root,28)
    root = insert(root,78)
    print(LCA(root,28,78))
    print(LCA(root,6,9))