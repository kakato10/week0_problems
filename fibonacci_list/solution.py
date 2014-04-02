def nth_fib_lists(listA, listB, n):
    result = []
    if listA == [] and listB == []:
        result = listA
    else:
        for i in range(0, n + 1):
            if i == 0:
                result = []
            if i == 1:
                result = listA
            elif i == 2:
                result = listB
            elif i > 2:
                nth_fib_lists2 = nth_fib_lists(listA, listB, i - 2)
                for j in (result):
                    (nth_fib_lists2).append(j)
                result = nth_fib_lists2

    return result
