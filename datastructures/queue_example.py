from Queue import Queue
from Nodes import Node

# New Queue instance
QueueInstance = Queue(maxSize=10)

# We generate {x} of Nodes using a loop.
for num in range(10):
    # we assign a value to item[x] and push it inside the Queue.
    item = Node(value=num)
    QueueInstance.enqueue(item)


# Print the Queue.
print(QueueInstance.getQueue())


