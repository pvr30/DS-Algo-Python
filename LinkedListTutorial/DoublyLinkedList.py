"""
Doubly Linked List

"""

# Create Node For DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
        
    # create a linked list
    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = None
        node.next = None

    # insert a node at the begin of th linked list
    def insertBegin(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            # assign prev and next in newnode
            node.prev = None
            node.next = self.head

            # create link between cur head and new node
            self.head.prev = node
            self.head = node

    # insert a node at the end of the list
    def insertEnd(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            iter = self.head
            while iter.next:
                iter = iter.next
            # print(iter.data)
            node.next = None
            node.prev = iter
            iter.next = node

    # insert a node at given index
    def insertIndex(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            iter = self.head
            index = 0
            # reach before element to the given index
            while index < location - 1:
                iter = iter.next
                index += 1
            # make node's prev and next
            node.prev = iter
            node.next = iter.next

            # connect new node to before and after element
            iter.next.prev = node
            iter.next = node

    # traverse the list
    def traverse(self):
        iter = self.head
        while iter:
            print(iter.data, end=", ")
            iter = iter.next

    # reverse traversal
    def reversetraversal(self):
        iter = self.head
        # reach to the last node/tail
        while iter.next:
            iter = iter.next

        # start traversing from last
        while iter:
            print(iter.data, end=", ")
            iter = iter.prev

    # search for a given value
    def search(self, value):
        if self.head is None:
            return "The list is empty"
        else:
            iter = self.head
            while iter:
                if iter.data == value:
                    return iter.data
                iter = iter.next
            return "the value does not exist in list"
        
    # delete an element from beggning of the linkedlist
    def deleteBegin(self):
        if self.head is None:
            print("linked list is empty")
        else:
            nextnode = self.head.next
            self.head = nextnode
            nextnode.prev = None
    
    # delete an element from end of the list
    def deleteEnd(self):
        if self.head is None:
            print("linked list does not exist")
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            prevNode = tail.prev
            prevNode.next = None
            prevNode = None

    # delete a node from perticular index
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

    #  Reverse a linked list
    def reverseLinkedList(self):
        node = self.head

        while node:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.next

        self.head = node

def printLL(LL):
    for node in LL:
        print(node.data, end="->")

doublyLL = DoublyLinkedList()
doublyLL.createDLL(1)
printLL(doublyLL)
    
print()
doublyLL.insertBegin(2)
doublyLL.insertBegin(3)
doublyLL.insertBegin(4)

printLL(doublyLL)

print()
doublyLL.insertEnd(10)
doublyLL.insertEnd(20)
doublyLL.insertEnd(30)

printLL(doublyLL)

print()
doublyLL.insertIndex(100, 6)
doublyLL.insertIndex(200, 3)

printLL(doublyLL)

print()
doublyLL.traverse()

print()
doublyLL.reversetraversal()

print()
print(doublyLL.search(100))
print(doublyLL.search(1000))

print()
doublyLL.deleteBegin()
doublyLL.deleteBegin()
doublyLL.deleteBegin()

printLL(doublyLL)

print()
doublyLL.deleteEnd()
doublyLL.deleteEnd()
# doublyLL.deleteEnd()

printLL(doublyLL)

print()
doublyLL.deleteIndex(2)
printLL(doublyLL)

print()
doublyLL.reverseLinkedList()
printLL(doublyLL)