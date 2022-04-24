from Stack import Stack
from Nodes import Node

# New Stack instance
StackInstance = Stack(maxSize=10)

# We generate {x} of Nodes using a loop.
for num in range(10):
    # we assign a value to item[x] and push it inside the Stack.
    item = Node(value=num)
    StackInstance.push(item)


# Print the Stack.
print(StackInstance.getStack())


