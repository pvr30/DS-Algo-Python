# Queue Using Linked List

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

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.queue]
        return " ".join(values)
    
    def isEmpty(self):
        return self.queue.head == None

    def enqueue(self, value):
        node = Node(value)
        if self.queue.head is None:
            self.queue.head = node
        else:
            iter = self.queue.head
            while iter.next:
                iter = iter.next

            # add element at the end of the queue
            iter.next = node
            node.next = None
    
    def dequeue(self):
        nodeValue = self.queue.head
        self.queue.head = nodeValue.next
        return nodeValue.value
        
    def peek(self):
        nodeValue = self.queue.head
        return nodeValue.value



customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)

print(customQueue)

print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue)

print(customQueue.peek())
print(customQueue)

