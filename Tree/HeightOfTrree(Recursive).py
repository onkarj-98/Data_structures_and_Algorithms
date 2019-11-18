'''Find the height of binary Tree'''
class Node:
    def __init__(self,data): # basic structure of Tree
        self.right = None
        self.left = None
        self.data = data

def heightOfTree(root):
    if root is None: # base case
        return 0 # This is important in python otherwise face type error
    else:
        return(1+ max(heightOfTree(root.left), heightOfTree(root.right)))


root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(9)
root.left.left.left = Node(7)
root.left.left.left.left = Node(10)
print(heightOfTree(root))




'''Basically we go down for each subtree and check untill base case happens, we add +1 for the root'''