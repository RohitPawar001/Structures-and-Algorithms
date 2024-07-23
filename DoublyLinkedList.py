class Node:
    
    def __init__(self, data:any) -> None:
        self.data = data
        self.prev = None
        self.next = None
        
        
class Doubly_Linked_list:
    
    def __init__(self) -> None:
        self.head = None
    
    
    #append function append the new_node at the end of dll
    def append(self, data:any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
            
      
    #append_at_begining append the node to the begining of the dll      
    def append_at_begining(self, data:any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            next = self.head
            self.head = new_node
            new_node.next = next
            next.prev = self.head
            
    
    #delete_node deletes the node from the doubly linked list         
    def delete_node(self,node) -> None:
        if self.head == None and node == None:
            return
        if self.head == node:
            self.head == node.next    
        if node.next is not None:
            node.next.prev = node.prev    
        if node.prev is not None:
            node.prev.next = node.next     
        node = None
        
    
    #traverse_forward function it start traversing the begining of the dll    
    def travrse_forward(self) -> None:
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()   
      
    
    #traverse_backward function starts traversing from the end of the dll       
    def traverse_backward(self) -> None:
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data,end=" ")
            temp = temp.prev
        
        
def main() -> None:  
    dll = Doubly_Linked_list()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append_at_begining(5)
    dll.travrse_forward()
    dll.delete_node(dll.head.next)
    dll.traverse_backward()
    
    
if __name__ == "__main__":
    main()

        
    