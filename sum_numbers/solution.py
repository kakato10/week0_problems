from random import randint


def get_me_some_integers(count, name):
    list_to_insert = []
    count_of_numbers = count
    filename = name
    file = open(filename, 'w')
    for i in range(0, count_of_numbers):
        list_to_insert.append(randint(1, 100))
    for i in list_to_insert:
        file.write(" ".join(str(i)))
    file.close()


def main(name):
    sum_numbers = 0
    filename = name
    file = open(filename, 'r')
    for i in file:
        for j in i:
            if j != ' ':
                sum_numbers = sum_numbers + int(j)
    file.close()
    return sum_numbers
