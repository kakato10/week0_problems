def is_increasing(seq):
    Temp1 = True
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            Temp1 = False
    return Temp1
