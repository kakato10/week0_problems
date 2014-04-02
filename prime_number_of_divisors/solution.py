def prime_number_of_divisors(n):
    k = 0
    if n < 0:
        n = - n
    for i in range(1, n + 1):
        if n % i == 0:
            k = k + 1
    temp = True
    if k == 1:
        temp = False
    else:
        for i in range(2, k):
            if k % i == 0:
                temp = False
    return temp
