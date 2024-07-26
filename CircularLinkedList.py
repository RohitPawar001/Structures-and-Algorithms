class Node:
    def __init__(self,data: any) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
     # this function add an node to the end of the circular linled list   
    def append_node(self,data:any) -> None:
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
        
    #this function add the node at the begining        
    def add_node_at_begining(self,data:any) -> None:
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
       
    #this function delete an node from the linked list      
    def delete_node_by_value(self,data:any) -> None:
        if not self.head:
            print("list is empty")
            return
        else:
            if self.head.data == data:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            else:
                current = self.head
                while current.next != self.head:
                    if current.next.data == data:
                        current.next = current.next.next
                        break
                    current = current.next
                                
    #this function used to show the data from the linked list   
    def print_list(self) -> None:
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


def main() -> None:  
      
    cll = CircularLinkedList()
    cll.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    cll.head.next = second
    second.next = third
    third.next = cll.head
    
    cll.append_node(5) 
    cll.add_node_at_begining(0)
    cll.delete_node_by_value(1)
    cll.print_list()
    
    
    
if __name__ == "__main__":
    main()