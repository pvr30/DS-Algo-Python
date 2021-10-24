"""
    Linear Search

    Time Complexity :- O(n)
    Space Complexity :- O(1)

"""
def linearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return arr[i]
    return -1

arr = [10, 3, 20, 60, 2]
print(linearSearch(arr, 20))
print(linearSearch(arr, 200))