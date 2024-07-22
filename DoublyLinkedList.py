class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        
        
    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    
dll = Doubly_Linked_list()
dll.head = Node(1)
second = Node(2)
third = Node(3)

dll.head.next = second
second.prev = dll.head
second.next = third
third.prev = second

dll.show()

        
    