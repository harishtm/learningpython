class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    

def insert(root, node):
    """ A utility function to insert a new node with the given key """
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    """ A utility function to do inorder tree traversal """
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == '__main__':
    rootnode = Node(50)
    insert(rootnode, Node(30))
    insert(rootnode, Node(20))
    insert(rootnode, Node(40))
    insert(rootnode, Node(70))
    insert(rootnode, Node(60))
    insert(rootnode, Node(80))
    inorder(rootnode)
    
