def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def quicksort(arr):
    quick_sort(arr, 0,  len(arr) - 1)
    return arr

arr = [9, 3, 7, 1, 4]
sorted_arr = quicksort(arr)
print("Отсортировано:", sorted_arr)