"""
Circular Doubly Linked List

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        node.prev = node
        node.next = node

    # insert a node at the begin of th linked list
    def insertBegin(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = node
            node.next = node
        else:
            tail = self.head
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            node.prev = tail
            node.next = self.head
            self.head = node
            # connect tail to new head
            tail.next = node

    # insert a node at the end of the list
    def insertEnd(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = node
            node.next = node
        else:
            tail = self.head
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            node.prev = tail
            node.next = self.head
            tail.next = node
            # connect head to new tail
            self.head.prev = node

    # insert a node at given index
    def insertIndex(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = node
            node.next = node
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1
            node.prev = iter
            node.next = iter.next
            iter.next.prev = node
            iter.next = node

    def traverse(self):
        node = self.head
        while node:
            print(node.data, end=", ")
            if node.next == self.head:
                break
            node = node.next


    def deleteBegin(self):
        if self.head is None:
            print("linked list is empty")
        else:
            tail = self.head
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head

    def deleteEnd(self):
        if self.head is None:
            print("linked list is empty")
        else:
            tail = self.head
            while tail:
                tail = tail.next
                if tail.next.next == self.head:
                    break
            # print(tail.data)
            tail.next = self.head
            self.head.prev = tail

    def deleteIndex(self, location):
        if self.head is None:
            print("linked list does not exist")
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1
            nextNode = iter.next.next
            iter.next = nextNode
            nextNode.prev = iter

def printCDLL(LL):
    for node in LL:
        print(node.data, end="->")

circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(1)
printCDLL(circularDLL)

print()
circularDLL.insertBegin(2)
circularDLL.insertBegin(3)
circularDLL.insertBegin(4)

printCDLL(circularDLL)

print()
circularDLL.insertEnd(10)
circularDLL.insertEnd(20)
circularDLL.insertEnd(30)

printCDLL(circularDLL)

print()
circularDLL.insertIndex(100, 0)
circularDLL.insertIndex(200, 4)
circularDLL.insertIndex(300, 7)

printCDLL(circularDLL)

print()
circularDLL.traverse()


print()
circularDLL.deleteBegin()
circularDLL.deleteBegin()
circularDLL.deleteBegin()



printCDLL(circularDLL)

print()
circularDLL.deleteEnd()
circularDLL.deleteEnd()
# circularDLL.deleteEnd()

printCDLL(circularDLL)

print()
circularDLL.deleteIndex(3)
printCDLL(circularDLL)


