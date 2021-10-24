# Selection Sort

"""
In case of selection sort we repeatedly find the maximum element and
move it to the sorted part of array to make unsorted part sorted

"""

# Time Complexity = O(n^2) , Space Complexity = O(1)


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[min_index], customList[i] = customList[i], customList[min_index]

    print(customList)



cuslist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selectionSort(cuslist)

"""
--- When to use Selection sort ?
        -When we have insufficient memory
        - Easy to implementation
--- When to avoid selection sort ?
        - when time is concern
"""