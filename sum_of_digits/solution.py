def sum_of_digits(n):
    sum_of_digits = 0
    if n < 0:
        n = n * (- 1)
    temp1 = True
    i = 0
    while temp1:
        if 10 ** i > n:
            temp1 = False
        else:
            temp = (n // (10 ** i)) % 10
            sum_of_digits = sum_of_digits + temp
            i = i + 1
    return sum_of_digits
