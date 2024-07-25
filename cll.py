class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append_node(self,data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next =  self.head
            
    def add_node_at_begining(self,data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            self.head.next = self.head
            
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            
    def delete_node_by_value(self,data):
        if not self.head:
            print("list is empty")
            return
        else:
            if self.head.data == data:
                next_head = self.head.next
                self.head = next_head
                
            else:
                current = self.head
                prev_current = None
                while (current.data != data) and (current.next != self.head):
                    prev_current = current
                    current = current.next
                prev_current.next = current
                
                
            
        
            
            
        
    def print_list(self):
        if not self.head:
            print("list is empty")
            return
        current = self.head
        while True:
            print(current.data,end = " ")
            current = current.next
            if current == self.head:
                print("back to start")
                break
            
            
            
            
    
cll = CircularLinkedList()
cll.head = Node(1)
second = Node(2)
third = Node(3)

cll.head.next = second
second.next = third
third.next = cll.head
cll.append_node(5) 
cll.add_node_at_begining(0)
cll.print_list()