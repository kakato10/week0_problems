def magic_square(matrix):
    sum1 = 0
    temp = True
    for i in matrix:
        sum1 = sum1 + i[matrix.index(i)]
    sum2 = 0
    for i in matrix:
        for j in range(0, len(matrix)):
            sum2 = sum2 + i[j]
        if sum2 != sum1:
            temp = False
        sum2 = 0
    for i in range(0, len(matrix)):
        for j in matrix:
            sum2 = sum2 + j[i]
        if sum2 != sum1:
            temp = False
        sum2 = 0
    for i in matrix:
        sum2 = sum2 + i[len(matrix) - 1 - matrix.index(i)]
    if sum2 != sum1:
        temp = False
    return temp
