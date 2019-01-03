class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    """ A utility function to insert a new node with given key in BST """
    
    # if the tree is empty, return the new node
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def inorder(root):
    """ A utility function to do inorder traversal of BST """
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


def minvaluenode(node):
    """ Given a non-empty binary search tree, return the node 
        with minum key value found in that tree
        Note that the entire tree does not need to be searched  
    """
    current = node
    
    while(current.left is not None):
        current = current.left

    return current


def deletenode(root, key):
    """Given a binary search tree and a key, this function 
       delete the key and returns the new root
    """
    if root is None:
        return root
    
    if key < root.key:
        root.left = deletenode(root.left, key)

    elif key > root.key:
        root.right = deletenode(root.right, key)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvaluenode(root.right)
        
        root.key = temp.key
        root.right = deletenode(root.right, temp.key)
    
    return root


if __name__ == '__main__':
    
    root = None
    root = insert(root, 50) 
    root = insert(root, 30) 
    root = insert(root, 20) 
    root = insert(root, 40) 
    root = insert(root, 70) 
    root = insert(root, 60) 
    root = insert(root, 80) 
      
    print("Inorder traversal of the given tree")
    inorder(root) 
      
    print("\nDelete 20")
    root = deletenode(root, 20) 
    print("Inorder traversal of the modified tree")
    inorder(root) 
      
    print("\nDelete 30")
    root = deletenode(root, 30) 
    print("Inorder traversal of the modified tree")
    inorder(root) 
      
    print("\nDelete 50")
    root = deletenode(root, 50) 
    print("Inorder traversal of the modified tree")
    inorder(root) 
