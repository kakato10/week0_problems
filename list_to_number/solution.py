def list_to_number(digits):
    number = 0
    for i in range(0, len(digits)):
        number = number + digits[len(digits) - 1 - i] * (10 ** i)
    return number
