"""
     Binary Tree Using Linked List

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")

leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee

rightChild = TreeNode("Cold")
coca = TreeNode("Coca")
fanta = TreeNode("Fanta")
rightChild.leftChild = coca
rightChild.rightChild = fanta


newBT.leftChild = leftChild
newBT.rightChild = rightChild

# PreOrder Traversal ..... rootnode -> leftchild -> rightchild
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print("\nPreOrderTraversal")
preOrderTraversal(newBT)


# InOrder Traversal ... leftchild -> rootnode -> rightchild
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print("\nInOrderTraversal")
inOrderTraversal(newBT)

# PostOrder Traversal ... leftchild -> rightchild -> rootnode
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


print("\nPostOrderTraversal")
postOrderTraversal(newBT)


# LevelOrderTraversal .... level by level

from collections import deque

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            print(root.data)
            if root.leftChild:
                q.append(root.leftChild)
            if root.rightChild:
                q.append(root.rightChild)


print("\nLevelOrderTraversal")
levelOrderTraversal(newBT)

#  Searching For an element in a binary tree

def searchBT(rootNode, value):
    if not rootNode:
        return
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            if root.data == value:
                return f"Successfully Found: {root.data}"
            if root.leftChild:
                q.append(root.leftChild)
            if root.rightChild:
                q.append(root.rightChild)
        return "Not Found ! Value Does not exists"

print(searchBT(newBT, "Coffee"))
print(searchBT(newBT, "Alcohol"))

# Insert a new node in Binary Tree using level order traversal

def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            
            if root.leftChild:
                q.append(root.leftChild)
            # insert a node at vacant leftchild place
            else:
                root.leftChild = newNode
                return

            if root.rightChild:
                q.append(root.rightChild)
            # insert a node at vacant rightchild place
            else:
                root.rightChild = newNode
                return

newNode = TreeNode("Green Tea")
insertBT(newBT, newNode)
levelOrderTraversal(newBT)

"""
     Delete a node from binary tree.
     - we can node directly delete a node bcoz each node is dependent on another node
     - so we need to replace deleted node with the deepest node of the bianry tree
     -- we need three method for that
        1. get the deepest node of tree
        2. delete the deepest node from binary tree
        3. replace deleted node with the deepestnode

"""

# 1. get the deepest node
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            
            if root.leftChild:
                q.append(root.leftChild)
            if root.rightChild:
                q.append(root.rightChild)
            deepestNode = root.data
        return deepestNode

# dnode = getDeepestNode(newBT)
# print(dnode)

# 2. delete the deepest node
def deleteDeepNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            if root.data is dNode:
                root.data = None
                return
            if root.leftChild:
                if root.leftChild.data is dNode:
                    root.leftChild = None
                    return
                else:
                    q.append(root.leftChild)
            if root.rightChild:
                if root.rightChild.data is dNode:
                    root.rightChild = None
                    return
                else:
                    q.append(root.rightChild)

#  3. Delete Node
def deleteNode(rootNode, Node):
    if not rootNode:
        return 
    else:
        q = deque([rootNode])
        while q:
            root = q.popleft()
            if root.data == Node:
                dNode = getDeepestNode(rootNode)    
                root.data = dNode
                deleteDeepNode(rootNode, dNode)
                return "success"
            if root.leftChild:
                q.append(root.leftChild)
            if root.rightChild:
                q.append(root.rightChild)
        return "Failed to delete"
            


print("\nAfter Delete Operation")
# dnode = getDeepestNode(newBT)
# deleteDeepNode(newBT, dnode)
print(deleteNode(newBT, "Cold"))
levelOrderTraversal(newBT)

# delete entire  binary tree
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

deleteBT(newBT)
levelOrderTraversal(newBT)