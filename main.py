def backpack(index, w, n,objects, weight, cost):
    if (weight > w):
        return  0
    if (index == n):
        return cost
    take = 0
    if (weight + objects[index][0] <=w):
        take = backpack(index+1, w, n,objects, weight + objects[index][0], cost + objects[index][1])

    skip = backpack(index+1, w, n, objects, weight, cost)

    return max(take, skip)