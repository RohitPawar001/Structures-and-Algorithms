class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None
        
def traverse_inorder(root):
    if root:
        traverse_inorder(root.left)
        print(root.val)
        traverse_inorder(root.right)
            
def traversePreorder(root):
    if root:
        print(root.val)
        traversePreorder(root.left)
        traversePreorder(root.right)
        
def traversePostorder(root):
    if root:
        traversePostorder(root.left)
        
        traversePostorder(root.right)
        print(root.val)
        
root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

traverse_inorder(root)
print("---")
traversePreorder(root)
print("---")
traversePostorder(root)