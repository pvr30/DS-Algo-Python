"""
    Binary Search
        - binary search is faster than linear search
        - half of remaining elements can be eliminated at a time, instead of
            eliminating them one by one.
        - binary search only works for sorted array
Time Complexity = O(logn)
"""

def binarySearch(arr, value):
    start = 0
    end = len(arr) - 1
    middle = (start+end) // 2

    while not(arr[middle] == value) and start <= end:

        # Search in left side of the array
        if value < arr[middle]:
            end = middle - 1

        # search in right side of the array
        elif value > arr[middle]:
            start = middle + 1
        middle = (start+end) // 2

    if arr[middle] == value:
        return middle
    else:
        return -1


arr = [1, 2, 3, 4, 5, 10, 20, 30]
print(binarySearch(arr, 30))
print(binarySearch(arr, 0))