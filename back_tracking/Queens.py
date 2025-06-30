def canPlace(row, col, positions):
    for i in range(row):
        if (positions[i] == col or
        positions[i] - i == col - row or
        positions[i] + i == row + col):
            return False
    return True

# если positions[4] = 3 то значит на пятой строке в 4 столбце стоит ферзь.
# Сложность O(N!)
def placeQuens(n, row, positions):# 1 поиск
    if (row == n):
        return True

    for col in range(n):
        if (canPlace(row, col, positions)):
            positions[row] = col

            if(placeQuens(n, row+1, positions)):
                return True

    return False

#Сложность O(N!)
def countSolutions(n, row, positions):
    total = 0
    if (row == n):
        return 1

    for col in range(n):
        if (canPlace(row, col, positions)):
            positions[row] = col
            total += countSolutions(n, row + 1, positions)
    return total

positions = [0] * 8

#print(placeQuens(8,0, positions))
print(countSolutions(8,0, positions))