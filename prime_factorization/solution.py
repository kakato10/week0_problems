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


def prime_factorization(n):
    if n == 0 or n == 1:
        return "Do not try to troll me"
    if is_prime(n):
        return [(n, 1)]
    prime_divisors = []
    for i in range(2, n):
        temp = is_prime(i)
        if temp == True and n % i == 0:
            prime_divisors.append(i)
    search_for_power = {}
    for divisor in prime_divisors:
        search_for_power[divisor] = 0
    for divisor in prime_divisors:
        while n % divisor == 0:
            n = n / divisor
            search_for_power[divisor] = search_for_power[divisor] + 1
    result = []
    for divisor in prime_divisors:
        if search_for_power[divisor] != 0:
            result.append((divisor, search_for_power[divisor]))
    return result
