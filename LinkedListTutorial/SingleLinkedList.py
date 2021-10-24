"""
  Singly Linked List

"""

# creation of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creation of single linkedlist
class SLinkedList:
    def __init__(self):
        self.head = None

    # Iteration method for printing nodes
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert node at the begnining of the linkedlist
    def insertBegin(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # insert node at the end of the linkedlist
    def insertEnd(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # traverse to the last node 
            tempNode = self.head
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = node

    # Insert a node/element at a perticular index
    def insertIndex(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1
            nextNode = iter.next
            iter.next = node
            node.next = nextNode
                
    # traverse the linkedlist
    def traverse(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next

    # search for an element in linkedlist
    def search(self, value):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node:
                if node.data == value:
                    return node.data
                node = node.next
            return "the value does not exist in list"


    # delete an element from beggning of the linkedlist
    def deleteBegin(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            self.head = self.head.next

    # delete an element from end of the list
    def deleteEnd(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            iter = self.head
            while iter.next.next:
                iter = iter.next
            iter.next = None
             
    # delete an element from perticular location
    def deleteIndex(self, location):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1
            iter.next = iter.next.next

    def reverseLinkedList(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

# Printing Linked List
def printLL(ll):
    for node in ll:
        print(node.data, end="->")

singleLL = SLinkedList()
# node1 = Node(1)
# node2 = Node(2)
# singleLL.head = node1
# singleLL.head.next = node2
singleLL.insertBegin(1)
singleLL.insertBegin(10)
singleLL.insertBegin(100)
printLL(singleLL)
print()

singleLL.insertEnd(20)
printLL(singleLL)
print()

singleLL.insertIndex(200, 3)
printLL(singleLL)

print()
singleLL.traverse()

print()
print(singleLL.search(20))
print(singleLL.search(2000))

# delete Operation
print()
singleLL.deleteBegin()
# singleLL.deleteBegin()
# singleLL.deleteBegin()

printLL(singleLL)

print()
singleLL.deleteEnd()
# singleLL.deleteEnd()
# singleLL.deleteEnd()

printLL(singleLL)

print()
singleLL.deleteIndex(1)
printLL(singleLL)

print()
singleLL.reverseLinkedList()
printLL(singleLL)

