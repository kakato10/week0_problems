def sum_of_divisors(n):
    list_divisors = []
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            list_divisors.append(i)
    for i in list_divisors:
        sum = sum + i
    return sum
