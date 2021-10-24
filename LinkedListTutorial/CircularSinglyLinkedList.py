"""
Circular Singly Linked List

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLL:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            # condition to prevent infinite loop
            if node.next == self.head:
                break
            node = node.next

    # creation of cirular linkedlist
    def createCLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node

    # insert element at the beggning of the list
    def insertBegin(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            tail = self.head
            # go to the last element in list
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            # print(tail.data)
            node.next = self.head
            self.head = node
            tail.next = node

    # insert element at the end of list
    def insertEnd(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            tail = self.head
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            node.next = tail.next
            tail.next = node

    # insert element at give index
    def insertIndex(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1
            node.next = iter.next
            iter.next = node

    # traverse a list
    def traverse(self):
        if self.head is None:
            print('the linked list does not exist')
        else:
            iter = self.head
            while iter:
                print(iter.data, end=", ")
                if iter.next == self.head:
                    break
                iter = iter.next

    # searching for an element in a linkedlist
    def search(self, value):
        if self.head is None:
            return "The list is empty"
        else:
            iter = self.head
            while iter:
                if iter.data == value:
                    return iter.data
                if iter.next == self.head:
                    return "Value Not Found"
                iter = iter.next
            

    # delete a node from beggning of the list
    def deleteBegin(self):
        if self.head is None:
            print("The list is empty")
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
            print("The list is empty")
        else:
            tail = self.head
            while tail.next:
                if tail.next.next == self.head:
                    break
                tail = tail.next
            tail.next = self.head
    
    def deleteIndex(self, location):
        if self.head is None:
            print("The list is empty")
        else:
            iter = self.head
            index = 0
            while index < location - 1:
                iter = iter.next
                index += 1 
            nextnode = iter.next
            iter.next = nextnode.next

    def reverseLinkedList(self):
        prev = None
        current = self.head
        
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        print(tail.data)

        while current != tail:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


def printLL(LL):
    for node in LL:
        print(node.data, end="->")


circularSLL = CircularSinglyLL()
circularSLL.createCLL(1) 

printLL(circularSLL)

print()
circularSLL.insertBegin(2)
circularSLL.insertBegin(3)
circularSLL.insertBegin(4)


printLL(circularSLL)


print()
circularSLL.insertEnd(50)
circularSLL.insertEnd(60)
circularSLL.insertEnd(70)
printLL(circularSLL)


print()
circularSLL.insertIndex(100, 2)
circularSLL.insertIndex(200, 4)
circularSLL.insertIndex(1000, 0)
circularSLL.insertIndex(400, 10)
printLL(circularSLL)

print()
circularSLL.traverse()

print()
print(circularSLL.search(100))
print(circularSLL.search(10000))


print()
circularSLL.reverseLinkedList()
printLL(circularSLL)

# delete operations
print()
# circularSLL.deleteBegin()
# circularSLL.deleteBegin()
# circularSLL.deleteBegin()

# printLL(circularSLL)


# print()
# circularSLL.deleteEnd()
# circularSLL.deleteEnd()
# circularSLL.deleteEnd()

# printLL(circularSLL)


# print()
# circularSLL.deleteIndex(0)
# # circularSLL.deleteIndex(2)
# circularSLL.deleteIndex(4)
# printLL(circularSLL)