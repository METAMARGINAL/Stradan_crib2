#┌────────────┬────────────────┬──────────────────┬────────────────┐
#│ Сложность  │ Лучший случай  │ Средний случай   │ Худший случай  │
#├────────────┼────────────────┼──────────────────┼────────────────┤
#│   Время    │     O(2ⁿ)      │      O(2ⁿ)        │     O(2ⁿ)      │
#├────────────┼────────────────┼──────────────────┼────────────────┤
#│  Память    │     O(2ⁿ)      │      O(2ⁿ)        │     O(2ⁿ)      │
#└────────────┴────────────────┴──────────────────┴────────────────┘


def grayCode(n):
    return recur(n, 1, [0])

def recur(n, base, nums):
    if n == 0:
        return nums
    # Create mirrored version with base added
    temp = []
    for i in range(len(nums)):
        temp.append(nums[len(nums)-1-i] + base)
    # Combine with original and recurse
    return recur(n-1, base*2, nums + temp)

print(grayCode(4))