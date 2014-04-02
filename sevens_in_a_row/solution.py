def sevens_in_a_row(arr, n):
    temp = False
    k = 0
    for i in range(0, len(arr)):
        if (arr[i] == 7):
            k = k + 1
            if k == n:
                temp = True
        else:
            k = 0
    return temp
