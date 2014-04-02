def nth_fibonacci(n):
    result = 0
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            result = 1
        if i > 2:
            result = result + nth_fibonacci(i - 2)
    return result
