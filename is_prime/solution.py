def is_prime(n):
    temp = True
    if n < 0:
        n = - n
    if n == 1 or n == 0:
        temp = False
    else:
        for i in range(2, n):
            if n % i == 0:
                temp = False
    return temp
