class Node:
    def __init__(self,data): #constructor to create new Tree
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
        root.right = insert(root.right, data)
    return root
def travers(root,path,k): # root for given tree and path for k element
    if root is None:
        return
    path.append(root.data)
    # stores this node in path, The node will be removed if not in path from root to k
    if root.data == k: # check k found on its root
        return True
    # check for k in left or right sub-tree
    if((root.left != None and travers(root.left,path,k))or (root.right != None and travers(root.right,path,k))):
        return True
    #if not present in sub-Tree rooted with with , remove root from path and rerurn false
    path.pop()
    return False
def findLCA(root,n1,n2):
    path1 = [] #To store path to n1 and n2 from the root
    path2 = []
    if(not travers(root,path1,n1) or not travers(root,path2,n2)): # if either n1 or n2 is not present, return -1
        return -1
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
if __name__ == '__main__':
    root = None
    root = insert(root,1)
    root = insert(root,2)
    root = insert(root,3)
    root = insert(root,4)
    root = insert(root,5)
    root = insert(root,6)
    root = insert(root,7)
    number = findLCA(root,4,5)
    print(number)
   # number = findLCA(root,4,6)
    #print(number)
#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)
#print("LCA(4,5) = %d" %(findLCA(root,4,5)))


