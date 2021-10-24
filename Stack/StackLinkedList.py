# Stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.stack]
        return "\n".join(values)

    def isEmpty(self):
        return self.stack.head == None

    def push(self, value):
        node = Node(value)
        node.next = self.stack.head
        self.stack.head = node

    def pop(self):
        if self.stack.head == None:
            return "stack is empty"
        else:
            nodeValue = self.stack.head.value
            self.stack.head = self.stack.head.next
            return nodeValue

    def peek(self):
        if self.stack.head == None:
            return "stack is empty"
        else:
            nodeValue = self.stack.head.value
            return nodeValue

customstack = Stack()
print(customstack.isEmpty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
print()
customstack.pop()
print(customstack)

print()
print(customstack.peek())