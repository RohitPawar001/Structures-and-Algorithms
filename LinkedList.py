#creating class Node to store the data and the pointer to the next node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
#creating LinkedList to point towards the head Node of the list      
class LinkedList:
    def __init__(self):
        self.head = None
     
    #created the show function to iterate over the linkedlist  
    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next 
      
    #apend_node_at_first it will add the next node into the first position      
    def apend_node_at_first(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            prev_node = self.head
            self.head = new_node
            self.head.next = prev_node
        
    
        
ll = LinkedList()
ll.head = Node(1)
second_node = Node(2)
third_node = Node(3)
ll.head.next = second_node
second_node.next = third_node

ll.show()

ll.apend_node_at_first(0)

ll.show()



