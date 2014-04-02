def is_an_bn(word):
    temp = True
    k1 = 0
    k2 = 0
    if len(word) % 2 == 1:
        temp = False
    else:
        for i in range(0, len(word) // 2):
            if word[i] == 'a':
                k1 = k1 + 1
            else:
                temp = False
            if word[(len(word) // 2) + i] == 'b':
                k2 = k2 + 1
            else:
                temp = False

    if word == '' or (k1 == k2 and temp):
        temp = True
    return temp
