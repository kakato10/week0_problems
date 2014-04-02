import sys


def main():
    count = 0
    the_file = []
    choose = ['chars', 'words', 'lines']
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        file = open(filename, 'r')
        the_file = file.read()
        if sys.argv[1] == choose[0]:
            count = len(the_file)
        elif sys.argv[1] == choose[1]:
            count = 1
            for i in range(0, len(the_file) - 1):
                if the_file[i] == ' ' or (the_file[i] == '\n' and the_file[i + 1] != '\n'):
                    count = count + 1
        elif sys.argv[1] == choose[2]:
            for i in the_file:
                if i == '\n':
                    count = count + 1
    else:
        print('Not enough arguements')
    print (count)
    return count

if __name__ == '__main__':
    main()
