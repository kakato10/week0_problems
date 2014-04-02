def is_prime(n):
    temp = True
    if n < 0:
        n = - n
    if n == 1:
        temp = False
    else:
        for i in range(2, n):
            if n % i == 0:
                temp = False
    return temp


def goldbach(n):
    candidates = []
    result = []
    for i in range(1, n - 1):
        if is_prime(i):
            candidates.append(i)
    for i in candidates:
        for j in candidates:
            if i + j == n and (i, j) not in result and (j, i) not in result:
                result.append((i, j))
    return result
