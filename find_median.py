def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i

def FindMedian(arr, k, left, right):
    if left <= right:
        p = partition(arr, left, right)
        if p < k:
            return FindMedian(arr, k, p + 1, right)
        elif p > k:
            return FindMedian(arr, k, left, p - 1)
        else:
            return arr[p]

def findMedian(arr):
    n = len(arr)
    if n % 2 == 1:
        return FindMedian(arr, n // 2, 0, n - 1)
    else:
        left = FindMedian(arr, n // 2 - 1, 0, n - 1)
        right = FindMedian(arr, n // 2, 0, n - 1)
        return (left + right) / 2

array = [4, 1, 10, 9, 7, 12, 8, 2, 15]
print("Медиана:", findMedian(array))