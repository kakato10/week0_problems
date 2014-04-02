from random import randint


def print_file(name):
    filename = name
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content


def main(count, name):
    list_to_insert = []
    count_of_numbers = count
    filename = name
    file = open(filename, 'w')
    for i in range(0, count_of_numbers):
        k = randint(1, 100)
        list_to_insert.append(k)
    making_string = ''
    for element in list_to_insert:
        making_string = making_string + str(element) + '\n'
    file.write(making_string)
    file.close()
