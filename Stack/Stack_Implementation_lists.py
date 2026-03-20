class StackUsingLists:
    def __init__(self):
        self.__stack =[]

    def push(self,data: int):
        self.__stack.append(data)
        return f"Pushed {data} into the stack"
    
    def size(self):
        return f"Stack size is {len(self.__stack)}"
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def pop(self):
        if self.is_empty():
            return "No elements to pop"
        return f"Popped element :{self.__stack.pop()}"
    
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return f"Top element :{self.__stack[-1]}"

stack = StackUsingLists()

print(stack.is_empty())
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.size())
print(stack.pop())
print(stack.top())
    