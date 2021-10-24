# Binary Search Tree

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# insert a node in a bst 
def insert(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue

    # insert element in left side of a tree
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insert(rootNode.leftChild, nodeValue)
    
    # insert element in right side of a tree
    elif nodeValue >= rootNode.data:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insert(rootNode.rightChild, nodeValue)

newBST = BSTNode(None)

insert(newBST, 70)
insert(newBST, 50)
insert(newBST, 90)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 80)
insert(newBST, 100)
insert(newBST, 20)
insert(newBST, 40)



# print(newBST.data)
# print(newBST.leftChild.data)
# print(newBST.rightChild.data)


# PreOrder Traversal ...  rootnode -> leftchild -> rightchild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print("\nPreOrderTraversal")
preOrderTraversal(newBST)


# InOrder Traversal ... leftchild -> rootnode -> rightchild
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print("\nInOrderTraversal")
inOrderTraversal(newBST)

# PostOrder Traversal ... leftchild -> rightchild -> rootnode
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


print("\nPostOrderTraversal")
postOrderTraversal(newBST)


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
levelOrderTraversal(newBST)

# search for a node in a binary search tree  time complexity: O(logN)
def searchBST(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("value found")
    
    # searching for left side of the tree
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("value found")
        else:
            searchBST(rootNode.leftChild, nodeValue)
    
    # searching for right side of the tree.
    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue:
            print("value found")
        else:
            searchBST(rootNode.rightChild, nodeValue)

# delete a node from a binary tree

# find min node value in a bst
def find_min(rootNode):
    if rootNode.leftChild is None:
        return rootNode
    return find_min(rootNode.leftChild)

# find max node value in a bst
def find_max(rootNode):
    if rootNode.rightChild is None:
        return rootNode
    return find_max(rootNode.rightChild)

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)

    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    
    else:

        # condition 1: having no child
        if not rootNode.leftChild and not rootNode.rightChild:
            rootNode = None

        # condition 2 : one child only

        # having right child or not having leftchild
        elif not rootNode.leftChild:
            rootNode = rootNode.rightChild

        # having leftchild or not having rightchild
        elif not rootNode.rightChild:
            rootNode = rootNode.leftChild

        # condition 3 : having two child
        else:
            temp = find_min(rootNode.rightChild) # get min node from right subtree
            rootNode.data = temp.data  # replace it 
            rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) #delete it
    return rootNode


searchBST(newBST, 20)
searchBST(newBST, 90)

print((find_min(newBST)))
print((find_max(newBST)))

print("After Delete Operation")
deleteNode(newBST, 90)
levelOrderTraversal(newBST)