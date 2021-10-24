# Create Stack Using Deque

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def __str__(self):
        values = [str(x) for x in self.container]
        return "-".join(values)

    def isEmpty(self):
        return len(self.container) == 0
    
    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print()

customStack.pop()
print(customStack)

print(customStack.peek())
print(customStack)