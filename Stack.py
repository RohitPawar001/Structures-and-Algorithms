# stack follows Last In First Out(LIFO) principle 
# LIFO means add the element at the last and start removing from the first element

stack = []

#append() method is used to add an element to the stack at the last position
print("adding an element to the stack ie LO \n")
for element in range(0,5):
    stack.append(element)
    print(stack)

#pop() method removes the first element from the last
print("removing an element from stack ie FO \n")
for element in range(len(stack)):
    stack.pop()
    print(stack)
