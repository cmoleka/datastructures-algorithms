class Stack:
    """
    Stack data structure
    A stack is an abstract data type that holds an ordered, linear sequence of items.
    In contrast to a queue, a stack is a last in, first out (LIFO) structure.
    """
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
    
    """
        getStack: returns the stack items.
    """
    def getStack(self):
        return self.stack

    """
        push: Adds an {item} to the stack.
    """
    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
            print(f"""
                /// Stack is adding the following: {item}.
                /// Current Stack top: 
                {self.peek()}
            """)        
        else:
            print(f"""
             ------------------------------------------------
             Our stack is full, item: {item} cannot be added.
             Please decrease the number of items.
             ------------------------------------------------
                """)

    """
        pop: removes top item of our stack. *top item is the last item added*
    """
    def pop(self):
        self.stack.pop()

        
    """
        peek: Returns the {item} at the top of our stack.
    """
    def peek(self):
        return self.stack[len(self.stack) - 1]

    """
        size: Returns the size of our stack.
    """
    def size(self):
        return len(self.stack)

    """
        isEmpty: Returns {True} if the stack is empty and {False} if its not.
    """
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    """
        isFull: Returns {True} if the stack is full and {False} if its not.
    """
    def isFull(self):
        if len(self.stack) == self.maxSize:
            return True
        else:
            return False
