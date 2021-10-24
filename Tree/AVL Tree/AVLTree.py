# AVL Tree

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

# PreOrder Traversal ...  rootnode -> leftchild -> rightchild
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# InOrder Traversal ... leftchild -> rootnode -> rightchild
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# PostOrder Traversal ... leftchild -> rightchild -> rootnode
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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

# getHeight of a node
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

# right rotation
def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# left rotation
def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# get Balance Value
def getBalance(rootNode):
    if not rootNode:
        return 0
    # return the difference
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)

    # find place on left side
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)

    # find place on right side
    elif nodeValue > rootNode.data:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # Left-Left Condition (LL)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)

    # Left-Right Condition (LR)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    # Right-Right Condition (RR)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)

    # Right-Left Condtion (RL)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode

# delete a node from a avl tree

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
    if not rootNode:
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

    # balance the avl tree
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # left-left condition
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)

    # right-right condition
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)

    # left-right condition
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    # right-left condition
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode

# search for a node in a AVL search tree  time complexity: O(logN)
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

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
# newAVL = insertNode(newAVL, 20)


levelOrderTraversal(newAVL)

# delete
print("\nAfter Deletion")
newAVL = deleteNode(newAVL, 15)

levelOrderTraversal(newAVL)



