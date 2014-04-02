def count_consonants(str):
    count = 0
    str2 = str.lower()
    for i in range(0, len(str2)):
        if str2[i] in 'qwrtpsdfghjklzxcvbnm':
            count = count + 1
    return count
