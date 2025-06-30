def BinarySearch(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if (arr[mid] == x):
            return mid
        else:
            if (arr[mid] > x):
                end = mid - 1
            else:
                if (arr[mid] < x):
                    start = mid + 1

    return -1


def RecursiveBinarySearch(arr, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if (arr[mid] == x):
        return mid
    elif (arr[mid] < x):
        return RecursiveBinarySearch(arr, x, mid+1, end)
    else:
        return RecursiveBinarySearch(arr, x, start, mid-1)

print(BinarySearch([1, 2, 3, 4, 5], 4))
print(RecursiveBinarySearch([1, 2, 3, 4, 5], 5, 0, 4))