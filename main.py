def cubi(n):
    if n == 1:
        return 1
    else:
        return n*n*n + cubi(n-1)


def cubi2(n):
    result = 0
    for i in range(1, n+1):
        result += i*i*i
    return result

print(cubi2(3))