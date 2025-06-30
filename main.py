
def Recursive_binarySearch(arr, f, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if  arr[mid] == f:
        return mid
    if arr[mid] > f:
       return Recursive_binarySearch(arr, f, left, mid - 1)
    else:
       return Recursive_binarySearch(arr, f, mid + 1, right)

def binarySearch(arr, f):
    left = 0
    right = len(arr) - 1

    if left > right:
        return -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == f:
            return mid
        elif f < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

print(binarySearch([1, 2, 3, 4, 5], 5))