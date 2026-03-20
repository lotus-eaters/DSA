class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self,data):
        newNode = Node(data)
        self._size += 1
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        self.tail.next = newNode
        self.tail = newNode
        return f"Added {data} to queue"
    
    def front(self):
        if self.size() == 0:
            return f"Queue is empty"
        return f"Front element is {self.head.data}"
    
    def dequeue(self):
        if self.size() == 0:
            return f"Queue is empty"
        dataTobeReturned = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return f"Removed element {dataTobeReturned}"

queue = QueueUsingLinkedList()

print(queue.is_empty())
print(queue.size())
print(queue.enqueue(3))
print(queue.enqueue(5))
print(queue.enqueue(7))
print(queue.size())
print(queue.dequeue())
