def count_words(arr):
    words = {}
    for word in arr:
        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1

    return words
