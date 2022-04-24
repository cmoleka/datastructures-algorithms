class Queue:
    """
        A queue is an abstract data type that holds an ordered, linear
        sequence of items. You can describe it as a first in, first out (FIFO) structure.
        The first element to be added to the queue will be the first element to be removed
        from the queue.
    """
    def __init__ (self, maxSize):
        self.queue = []
        self.maxSize = maxSize
        self.front = 0
        self.rear = -1

    """
        getQueue: Returns {list} of Queue.
    """
    def getQueue(self):
        return self.queue

    """
        isFull: Returns {Boolean} if Queue is full or empty.
    """
    def isFull(self):
        if self.rear + 1 == self.maxSize:
            print("Queue is full")
            return True
        else:
            print("Queue is  not full")
            return False

    """
        isEmpty: Returns {Boolean} if Queue is empty or not.
    """
    def isEmpty(self):
        if self.front > self.rear:
            print("Queue is empty")
            return True
        else:
            print("Queue is not empty")
            return False

    """
        enqueue: Inserts {item} inside the queue.
    """
    def enqueue(self, data):
        if self.isFull() is True:
            pass
        else:
            self.rear = self.rear + 1
            self.queue.insert(self.rear, data)
    
    """
        dequeuek: Removes {item} from the queue and return it.
    """
    def dequeue(self):
        dequeued_item = None
        if self.isEmpty():
            print("Queue is empty")
            pass
        else:
            dequeued_item = self.queue.pop(self.front)
            self.front = self.front + 1
        return dequeued_item



