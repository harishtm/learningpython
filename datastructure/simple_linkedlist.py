class Node:
    """
        Creating a node
        info field / link field
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
        Linked List
    """
    
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    def display(self):
        current = self.head
        while current is not None:
            # print(current.data, end="=>")
            print(hex(id(current)), current.__dict__, end=",")
            print("\n")
            current = current.next


if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(20)
    l.append(30)
    l.append(40)
    l.append(50)
    l.append(60)
    l.append(70)
    l.display()
