# Binary Tree using Python List

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # insert a new node in binary tree
    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is Full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "successfully inserted"

    def search(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Found"
        return "Not Found"


    # PreOrder Traversal
    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index]) #rootNode
        self.preOrderTraversal(index * 2) # leftChild
        self.preOrderTraversal(index * 2 + 1) # rightChild

    # InOrder Traversal
    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2) # leftChild
        print(self.customList[index]) #rootNode
        self.inOrderTraversal(index * 2 + 1) # rightChild

    # PostOrder Traversal
    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2) # leftChild
        self.postOrderTraversal(index * 2 + 1) # rightChild
        print(self.customList[index]) #rootNode

    # level order traversal
    def levelOrderTraversal(self, index=1):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    # delete a node from a binary tree
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "there is no element in a tree"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "successfully deleted"
        return "failed to deleted"
            
    # delete entire binary tree
    def deleteBT(self):
        self.customList = None

newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))

print(newBT.search("Tea"))
print(newBT.search("Cold"))


newBT.insert("Tea")
newBT.insert("Coffee")

print("\nPreOrderTraversal")
newBT.preOrderTraversal()

print("\nInOrderTraversal")
newBT.inOrderTraversal()

print("\nPostOrderTraversal")
newBT.postOrderTraversal()

print("\nLevelOrderTraversal")
newBT.levelOrderTraversal()

print()
print(newBT.deleteNode("Tea"))
newBT.levelOrderTraversal()