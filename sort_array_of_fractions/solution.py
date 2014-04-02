def sort_fractions(fractions):
    new_fractions = []
    new_fractions2 = []
    for i in fractions:
        for j in range(0, 2):
            new_fractions.append(i[j])
    for i in range(0, len(new_fractions), 2):
        for j in range(i + 2, len(new_fractions), 2):
            if new_fractions[i] / new_fractions[i + 1] > new_fractions[j] / new_fractions[j + 1]:
                temp1 = new_fractions[i]
                new_fractions[i] = new_fractions[j]
                new_fractions[j] = temp1
                temp2 = new_fractions[i + 1]
                new_fractions[i + 1] = new_fractions[j + 1]
                new_fractions[j + 1] = temp2
                j = i + 2

    for i in range(0, len(new_fractions), 2):
        new_fractions2.append((new_fractions[i], new_fractions[i + 1]))

    return new_fractions2
