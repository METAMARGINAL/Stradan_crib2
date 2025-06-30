#┌────────────┬───────────────┬────────────────┬──────────────┐
#│ Сложность  │ Лучший случай │ Средний случай │ Худший случай│
#├────────────┼───────────────┼────────────────┼──────────────┤
#│   Время    │   O(n log n)  │   O(n log n)   │  O(n log n)  │
#├────────────┼───────────────┼────────────────┼──────────────┤
#│   Память   │     O(n)      │      O(n)      │     O(n)     │
#└────────────┴───────────────┴────────────────┴──────────────┘

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)

