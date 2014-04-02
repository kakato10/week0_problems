def contains_digits(number, digits):
    temp1 = False
    for i in range(0, len(digits)):
        if str(digits[i]) in str(number):
            temp1 = True
        else:
            temp1 = False
            break
    if len(digits) == 0:
        temp1 = True
    return temp1
