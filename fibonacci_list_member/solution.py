def nth_fib_lists(listA, listB, n):
    stringA = ''
    for element in listA:
        stringA = stringA + str(element)
    stringB = ''
    for element in listB:
        stringB = stringB + str(element)
    result = ''
    if n == 0:
        return result
    if n == 1:
        return stringA
    if n == 2:
        return stringB
    if n > 2:
        for i in range(0, n):
            result = nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)
    return result


def member_of_nth_fib_lists(listA, listB, needle):
    string_needle = ''
    for element in needle:
        string_needle = string_needle + str(element)
    if string_needle in nth_fib_lists(listA, listB, 6):
        return True
    return False


def main():
    print (member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4]))
    print (member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
    print (member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
    print (member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    main()
