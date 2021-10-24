# Bucket Sort

"""
 -- Create buckets and distribute elements of array into buckets
 -- Sort buckets individually
 -- Merge buckets after sorting

"""

"""
 -- Number of buckets = round(sqrt(number of elements)
 -- Appropriate bucket = ciel(Value * number of buckets / maxValue)

"""
import math
from InsertionSort import insertionSort


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

cuslist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(bucketSort(cuslist))