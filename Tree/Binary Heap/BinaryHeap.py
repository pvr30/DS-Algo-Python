# Heap


class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = (size + 1)

# peek of heap top most element of the tree
def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

# size of heap count only filled element
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# traverse tree
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i], end=" ")


# insertion in heap

# heapify method to adjust the heap tree after inserting an element for maintain property of min or max heap
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)  # come from leftChild = 2 * i

    if index <= 1:
        return
    
    # for min heap
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    # for max heap
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "the heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

# Extraction/Deletion we can only delete root in heap and we can not delete any other element

# heapify method for extraction
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    # temp varible to store index
    swapChildIndex = 0

    # rech to last index
    if rootNode.heapSize < leftIndex:
        return
    
    # check for leftIndex
    elif rootNode.heapSize == leftIndex:
        # min heap
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        # max heap
        elif heapType == "Max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    
    # check for rightIndex
    elif rootNode.heapSize == rightIndex:

        # min heap
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChildIndex = leftIndex
            else:
                swapChildIndex = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChildIndex]
                rootNode.customList[swapChildIndex] = temp
            return

        # max heap
        elif heapType == "Max":
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChildIndex = leftIndex
            else:
                swapChildIndex = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChildIndex]
                rootNode.customList[swapChildIndex] = temp
            return
    heapifyTreeExtract(rootNode, swapChildIndex, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode


newHeap = Heap(5)
        
# print(sizeofHeap(newHeap))

# max heap
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 6, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 8, "Max")

print("Max Heap")
levelorderTraversal(newHeap)
print()
print(extractNode(newHeap, "Max"))
levelorderTraversal(newHeap)

# print()
# print(sizeofHeap(newHeap))


minHeap = Heap(5)

# min heap
insertNode(minHeap, 4, "Min")
insertNode(minHeap, 6, "Min")
insertNode(minHeap, 2, "Min")
insertNode(minHeap, 8, "Min")

print("\nMin Heap")
levelorderTraversal(minHeap)
print()
print(extractNode(minHeap, "Min"))
levelorderTraversal(minHeap)
