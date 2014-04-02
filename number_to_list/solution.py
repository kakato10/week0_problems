def number_to_list(n):
    temp = True
    numbers = []
    i = 0
    while temp:
        if (10 ** i) > n:
            break
        else:
            numbers.append((n // (10 ** i)) % 10)
            i = i + 1
    numbers2 = []
    temp = True
    i = len(numbers) - 1
    while temp:
        numbers2.append(numbers[i])
        if i == 0:
            temp = False
        i = i - 1

    return numbers2
