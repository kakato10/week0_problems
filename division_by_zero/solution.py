def count_numbers(numbers):
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        for another_number in sorted_numbers:
            if another_number // number not in sorted_numbers\
            and another_number != number and another_number // number != 0:
                sorted_numbers.append(another_number // number)
    return len(sorted_numbers)
