def count_substrings(haystack, needle):
    t = 0
    k = 0
    for i in range(0, len(haystack)):
        if needle[k] == haystack[i]:
            k = k + 1
            if k == len(needle):
                t = t + 1
                k = 0
        else:
            k = 0
    return t
