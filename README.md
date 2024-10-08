# Structures and Algorithms in python

<h1> 1.list </h1>
    Lists are ordered collections of data, It allows different types of elements in the list. The costly operation is inserting or deleting the element from the beginning of the List as all the elements are needed to be shifted. 
    <img src="https://github.com/user-attachments/assets/974869e3-a0ef-4762-8f4e-dab63c52af9b">

<h1>2. tuple </h1>
    tuple are same as list except they are immutable. immutable means once the tuple is created cannot add or remove elements from the tuple <br> to remove the element from the tuple we have to first typecast it into the another datatype.
    <br>
    tuple are enclosed within the () braces and elements are seperated by commas and it can store different datatypes 

<h1>3. sets </h3>
     
Sets are unordered collections of unique elements. In Python, you can create sets using curly braces {} or the set() constructor.
(~ # Create sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

**Union**
union_result = set_a | set_b
print("Union:", union_result)

**Intersection**
intersection_result = set_a & set_b
print("Intersection:", intersection_result)

**Difference**
difference_result = set_a - set_b
print("Difference:", difference_result)

**Membership testing**
print(2 in set_a)  # True
print(6 in set_a)  # False
~)

<h1>4.Stack</h1>
stack follows LIFO (last in last out ) priciple ie the lastly inserted elemetn is get removed first.
<br> in python the stack can be implemented using list.
<br> <img src = "https://github.com/user-attachments/assets/87984e52-035b-4af7-8069-6a4dc84d7d64" !>
<br> the element insertation and deletion done at the same end.
<br> we can perform two operation in stack ther are <br> 1.push <br> 2.pop

<h1>5.Queue</h1>
A queue in Python is a linear data structure that follows the First In First Out (FIFO) principle, meaning the first element added to the queue will be the first one to be removed. Think of it like a line of people waiting for a service, where the person who arrives first is served first.<br>
There are several ways to implement a queue in Python:<br>
<img src="https://github.com/user-attachments/assets/a01ea920-0d54-4963-a25b-1379d10dbe8c">

1.using lists<br>2.using queue.Queue<br>3.using 

<h1>bytearray</h1>
A binary array in Python typically refers to an array that contains binary data, which is data represented in the form of 0s and 1s. There are several ways to work with binary arrays in Python, depending on your specific needs. Here are a few common methods:<br>
1.using numpy <br>2.using array module <br>3.using lists <br>4.using bytearray

<h1>6.Dictionary</h1>
<br>A dictionary in Python is a collection of key-value pairs. Each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change, add, or remove items after the dictionary is created. They are also ordered as of Python 3.7, meaning the items have a defined order.
<br>
**Dictionary method**
<br>
Here are some useful dictionary methods:<br>

keys(): Returns a view object of all keys.<br>
values(): Returns a view object of all values.<br>
items(): Returns a view object of all key-value pairs.<br>
update(): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

<h1>7.Linked List</h1>
A linked list is a linear data structure where each element, called a node, contains a data part and a reference (or link) to the next node in the sequence. Linked lists are useful for dynamic memory allocation and efficient insertions and deletions.<br>

**Types of Linked Lists**<br>
Singly Linked List: Each node points to the next node.<br>
Doubly Linked List: Each node points to both the next and the previous node.<br>
Circular Linked List: The last node points back to the first node.<br>

**Node Class:** Defines the structure of a node with data and next attributes.<br>
**LinkedList Class:** Contains methods to insert nodes at the beginning and end, delete nodes, search for nodes, and print the list.<br>
**Example Usage:** Demonstrates how to create a linked list, insert nodes, search for a node, delete a node, and print the list.<br>


