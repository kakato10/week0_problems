def is_int_palindrom(n):
    temp1 = str(n)
    temp2 = temp1[:: - 1]
    return temp1 == temp2
