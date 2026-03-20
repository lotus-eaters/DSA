class QueueUsingList:
    def __init__(self):
        self.__queue = []
    
    def size(self):
        return len(self.__queue)
    
    def is_empty(self):
        return self.size()==0
    
    def enqueue(self,data):
        self.__queue.append(data)
        return f"Added {data} to queue"
    
    def front(self):
        if self.size() ==0:
            return f"Queue is empty"
        frontElement = self.__queue[0]
        return f"Front element of the queue is {frontElement} "
    
    def dequeue(self):
        if self.size() ==0:
            return f"Queue is empty"
        popElement = self.__queue.pop(0)
        return f"Removed element : {popElement}"
    
queue = QueueUsingList()

print(queue.is_empty())
print(queue.size())
print(queue.enqueue(3))
print(queue.enqueue(5))
print(queue.enqueue(7))
print(queue.size())
print(queue.dequeue())

