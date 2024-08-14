class Node:
    def __init__(self,key:any) -> None:
        self.val = key
        self.right = None
        self.left = None
 # this function executes the deletion operation in BST       
def deleteNode(root,key:any):
    if root is None:
        return root
    
    if key < root.val:
        root.left = deleteNode(root.left,key)
    elif key > root.val:
        root.right = deleteNode(root.right,key)
    else:
        if not root.right:
            return root.right
        elif not root.left:
            return root.left
        
        temp = minValNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right,temp.val)
    
    return root
# this function returns  the node which having the lowest value      
def minValNode(node):
    current = node
    while current.left:
        current = current.left
    return current
        
# this function performs the searching operation in BST
def searchElement(root, target:any) -> bool:
    if root is None:
        return False
    if root.val == target:
        return True
    if target < root.val:
        return searchElement(root.left, target)
    return searchElement(root.right, target)

# it will be traverse the node in inorder manner i.e left -> root -> right
def traverseInorder(root) -> None:
    if root:
        traverseInorder(root.left)
        print(root.val,end=" ")
        traverseInorder(root.right)
           
# it will be traverse the node in inorder manner  i.e root -> left -> right          
def traversePreorder(root) -> None:
    if root:
        print(root.val,end=" ")
        traversePreorder(root.left)
        traversePreorder(root.right)
        
# it will be traverse the node in inorder manner  i.e left -> right -> root       
def traversePostorder(root) -> None:
    if root:
        traversePostorder(root.left)
        traversePostorder(root.right)
        print(root.val,end=" ")
        
        
def main() -> None:
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)

    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(5)
    root.right.right = Node(7)

    print("Inorder traversal before deletion:")
    traverseInorder(root)
    print("\n---")
    print("Preorder traversal before deletion:")
    traversePreorder(root)
    print("\n---")

    root = deleteNode(root, 2)

    if searchElement(root, 3):
        print("3 is in BST")
    else:
        print("3 not in BST")

    print("Postorder traversal after deletion:")
    traversePostorder(root)
    print("\n---")
    
    

if __name__ == "__main__":
    main()