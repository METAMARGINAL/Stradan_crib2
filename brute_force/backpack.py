def backpack(index, w, n, obj, weight, cost):
    if (weight > w):
        return 0
    if (index == n):
        return cost
    take = 0
    if (weight + obj[index][0] <= w):
        take = backpack(index + 1, w, n, obj, weight + obj[index][0], cost +obj[index][1])
    skip = backpack(index + 1, w, n, obj, weight, cost)

    return max(take, skip)

capacity = 7
items = [(2, 10), (3, 5), (4, 15), (5, 7)]  # (вес, ценность)

print(backpack(0, capacity, 4, items, 0, 0 ))