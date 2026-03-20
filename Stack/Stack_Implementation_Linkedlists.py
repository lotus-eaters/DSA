class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self._size=0
        self.head=None
    
    def push(self,data):
        newNode = Node(data)
        self._size+=1
        if self.head is None:
            self.head = newNode
            return f"Added {data} to the stack"
        newNode.next = self.head
        self.head = newNode
        return f"Added {data} to the stack"
    
    def top(self):
        if self.head is None or self._size==0:
            return "Stack is Empty"
        return f"Top element is {self.head.data}"
    
    def pop(self):
        if self.head is None or self._size==0:
            return "Stack is empty"
        dataToPop = self.head.data
        self.head = self.head.next
        self._size-=1
        return f"Popped element is {dataToPop}"
    
    def size(self):
        return f"Stack size is {self._size}"

    def is_empty(self):
        if self._size == 0:
            return True 
        return False

stack = StackUsingLinkedList()

print(stack.is_empty())
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.size())
print(stack.pop())
print(stack.top())
       
