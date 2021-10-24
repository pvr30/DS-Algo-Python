"""
Insertion sort :-
    - divine the given array into two parts
    - take first element from unsorted array and find its correct
        position in sorted array
    - repeat until unsorted array is empty
"""


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    # print(customList)
    return customList

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cList)


"""
 -- when to use insertion sort ?
    - when we have insufficient memory
    - easy to implementation
    - when we have continuous inflow of numbers and we want to keep them sorted

 # -- when to avoid ?
    - when time is concern
"""
