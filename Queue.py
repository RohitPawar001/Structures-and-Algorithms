#queue follows First In First Out (FIFO) principle
# FIFO i.e starting element is first grt removed

queue = []

# insert an element into queue
print("initial queue\n",queue)
for element in range(4):
    queue.append(element)
    print(queue)
    
#deleting an element from queue
print("\n removing an element fron queue")
for element in range(len(queue)):
    queue.remove(queue[0])
    print(queue)

