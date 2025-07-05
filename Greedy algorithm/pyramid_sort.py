def heapify(arr, n, i):
    largest = i         # Инициализируем наибольший элемент как корень
    left = 2 * i + 1    # Левый потомок
    right = 2 * i + 2   # Правый потомок

    # Если левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок больше самого большого элемента на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Поменять местами
        heapify(arr, n, largest)  # Рекурсивно heapify на затронутом поддереве

def heap_sort(arr):
    n = len(arr)

    # Построить max-heap (пирамиду)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print(arr)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Поменять местами
        heapify(arr, i, 0)  # Вызвать heapify на уменьшенной куче

# Пример использования:
arr = [5, 3, 1, 4, 7, 9, 2, 0, 6]
heap_sort(arr)
print("Отсортированный массив:", arr)