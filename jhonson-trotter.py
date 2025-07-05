def find_max_mobile_element(permutation, direction):
    index = -1
    for i in range(len(permutation)):
        next_element_index = i + direction[i]

        if 0 <= next_element_index < len(permutation):
            if permutation[i] > permutation[next_element_index]:
                if index == -1 or permutation[i] > permutation[index]:
                    index = i
    return index


def change_direction(permutation, direction, mobile_element):
    for i in range(len(permutation)):
        if permutation[i] > mobile_element:
            direction[i] *= -1

def swap_element(permutation, direction, i, j):
    # Меняем местами элементы и их направления
    permutation[i], permutation[j] = permutation[j], permutation[i]
    direction[i], direction[j] = direction[j], direction[i]

def permutation_generator(n):
    # Начальная перестановка [1, 2, ..., n]
    permutation = list(range(1, n + 1))
    # Направление движения всех элементов (-1 означает влево)
    direction = [-1] * n

    print(permutation)

    # Находим индекс максимального подвижного элемента
    mobile_element_index = find_max_mobile_element(permutation, direction)

    while mobile_element_index != -1:
        mobile_element = permutation[mobile_element_index]
        next_index = mobile_element_index + direction[mobile_element_index]

        # Меняем местами подвижный элемент с тем, на который он указывает
        swap_element(permutation, direction, mobile_element_index, next_index)

        # Меняем направление всех элементов больше текущего подвижного
        change_direction(permutation, direction, mobile_element)

        print(permutation)

        # Обновляем индекс следующего подвижного элемента
        mobile_element_index = find_max_mobile_element(permutation, direction)

# Вызов функции для генерации всех перестановок из 3 элементов
permutation_generator(4)
