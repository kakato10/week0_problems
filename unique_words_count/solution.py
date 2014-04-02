def unique_words_count(arr):
    words = {}
    unique_words = []
    for word in arr:
        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1
    for word in words:
        unique_words.append(words[word])
    return len(unique_words)


def main():
    print (unique_words_count(["apple", "banana", "apple", "pie"]))
    print (unique_words_count(["python", "python", "python", "ruby"]))
    print (unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    main()
