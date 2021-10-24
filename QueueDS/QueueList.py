# Create Queue using List

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        values = [str(x) for x in self.queue]
        return " ".join(values)

    def isEmpty(self):
        return self.queue == []

    # enqueue/insert an element in queue
    def enqueue(self, value):
        self.queue.append(value)

    # dequeue/remove an element from queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[0]
        



customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())