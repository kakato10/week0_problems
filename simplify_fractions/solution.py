def simplify_fraction(fraction):
    rational_number = list(fraction)
    fract = 1
    for i in range(2, max(rational_number)):
        if (min(rational_number) % i == 0) and (max(rational_number) % i == 0) and i > fract:
            fract = i
    if fract != 1:
        rational_number[0] = int(rational_number[0] / fract)
        rational_number[1] = int(rational_number[1] / fract)
    if min(rational_number) == max(rational_number):
        rational_number[0] = 1
        rational_number[1] = 1
    return tuple(rational_number)
