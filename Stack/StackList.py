# Stack without size limit

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(v) for v in self.list]
        return "-".join(values)

    # check whethetr the stack isEmpty or not
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push an element in stack
    def push(self, value):
        self.list.append(value)

    # pop/remove a top element from the stack
    def pop(self):
        if self.isEmpty():
            return "the stack is empty"
        else:
            return self.list.pop()

    # peek/get a top element from the stack
    def peek(self):
        if self.isEmpty():
            return "the stack is empty"
        else:
            return self.list[-1]

    # delete entire stack
    def delete(self):
        self.list = None

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

customStack.delete()
# print(customStack)