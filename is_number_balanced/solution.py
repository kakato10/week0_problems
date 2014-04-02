def is_number_balanced(n):
    temp1 = False
    sum1 = 0
    sum2 = 0
    k = str(n)
    if len(k) == 1:
        temp1 = True
    elif len(k) % 2 == 0:
        for i in range(0, len(k) // 2):
            sum1 = sum1 + int(k[i])
            sum2 = sum2 + int(k[len(k) - i - 1])

    else:
        for i in range(0, (len(k) // 2) + 1):
            sum1 = sum1 + int(k[i])
            sum2 = sum2 + int(k[len(k) - i - 1])
    if sum1 == sum2:
        temp1 = True
    return temp1
