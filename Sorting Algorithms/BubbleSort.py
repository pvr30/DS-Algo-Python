# Bubble Sort
# Bubble sort is also referred as Sinking Sort
"""
In This Sorting algorithm we repeatedly compare each pair of adjacent
items and swap them if they are in wrong order

"""

# Time Complexity = O(n^2) , Space Complexity = O(1)

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)


# O(n) Time Complexity
def bubbleSortN(customList):
    for i in range(len(customList)-1):
        swapped = False
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
                swapped = True
        if not swapped:
             break
    print(customList)

cuslist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bubbleSort(cuslist)


"""
-- When to use bubble sort.
    - Space is Concern
    - Easy to implement
-- When to Avoid it?
    - Average time complexity is poor

"""