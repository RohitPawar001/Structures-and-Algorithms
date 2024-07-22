#creating class Node to store the data and the pointer to the next node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
#creating LinkedList to point towards the head Node of the list      
class LinkedList:
    def __init__(self):
        self.head = None
     
     
    #apend_node_at_first it will add the next node into the first position      
    def apend_node_at_first(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            prev_node = self.head
            self.head = new_node
            self.head.next = prev_node
        
    #this function insert the node at the end of the linked list
    def apend_node_at_end(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        end_node = None
        while temp:
            if temp.next == None:
                end_node = temp
            temp = temp.next
        end_node.next = new_node
        
        
    #This function insert a new node at a given position   
    def insert_node_at_position(self, new_data, position):
        new_node = Node(new_data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    raise IndexError("index is out of range")
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
     
    # delete_node function delete the entore node from the begining        
    def delete_node(self,position):
        if self.head is None:
            return
        index = 0
        current_node = self.head
        while current_node.next and index < position:
            previous = current_node
            current_node = current_node.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current_node.next 
            
    def delete_linked_list(self):
        current_node = self.head
        while current_node:
            previous_node = current_node
            current_node = current_node.next
            del previous_node
        self.head = None
        print("linked_list deleted successfully")
        
             
    #created the show function to iterate over the linkedlist  
    def show(self):
        
            temp = self.head
            while temp:
                print(temp.data,end = " ")
                temp = temp.next 
            print()
                          
def main():               
    linked_list = LinkedList()
    linked_list.head = Node(1)
    
    second_node = Node(2)
    third_node = Node(3)
    
    linked_list.head.next = second_node
    second_node.next = third_node
    
    linked_list.insert_node_at_position("new_node",1)
    
    print(linked_list.show())
    
    linked_list.delete_node(2)
    
    print(linked_list.show())
    
    linked_list.delete_linked_list()
    
    print(linked_list.show())
    
    

if __name__ == "__main__":
    main()



