"""
--- Merge Sort
        - MergeSort is an divide and conquer algorithm
        - divide the input array into two halves and we keep halving recursively until
            they become too small that cannot be broken further
        - merge halves by sorting them

    -- Time And Space Complexity Respectively = O(NlogN) and O(n)
"""



# merge two sorted arrays
def merge_sorted_arrays(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        # check if element of array a is less than element of array b
        # then increment small element's index
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        # check if element of array b is less than element of array a
        # then increment small element's index
        else:
            arr[k] = b[j]
            j += 1
        # increment k every time
        k += 1

    # fill the rest of the a's element in arr
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    # fill the rest of the b's element in arr
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

# merge sort function

def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2

    # divide into two parts from middle element
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge_sorted_arrays(left, right, arr)


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
mergeSort(cList)
print(cList)

test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [3],
    [9, 8, 7, 2],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    mergeSort(arr)
    print(arr)


"""
    -- When to us merge sort ?
        - when you need stable sort
        - when average expected time is O(NlogN)
    -- When to avoid ?
        - Space is concern
"""