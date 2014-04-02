def count_vowels(str):
    count = 0
    for i in range(0, len(str)):
        if str[i] in 'aeiouyAEIOUY':
            count = count + 1
    return count
