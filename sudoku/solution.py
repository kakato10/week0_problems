def sudoku_solved(sudoku):
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    temp_list = []
    result = True
    for i in sudoku:
        for j in range(0, len(sudoku)):
            temp_list.append(i[j])
        temp_list.sort()
        if len(temp_list) == 9 and temp_list != digits:
            result = False
    for i in range(0, len(sudoku)):
        for j in sudoku:
            temp_list.append(j[i])
        temp_list.sort()
        if len(temp_list) == 9 and temp_list != digits:
            result = False
    new_temp_list = []
    k = 0
    l = 0
    for i in range(l, l + 3):
        for j in range(k, k + 3):
            new_temp_list.append((sudoku[i])[j])
        new_temp_list.sort()
        if (i + 1) % 3 == 0 and len(new_temp_list) == 9 and new_temp_list != digits:
            result = False
        if (i + 1) % 3 == 0 and len(new_temp_list) == 9:
            new_temp_list = []
            if (k + 3) == (9):
                l = l + 3
                k = 0
            else:
                k = k + 3
    return result
