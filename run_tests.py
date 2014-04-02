import os
from subprocess import call


def testing_time(pattern):
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.startswith(pattern):
                print('***********************')
                print('Testing ' + root[2:])
                print('***********************')
                call(['python3', root + '/' + file])


def main():
    testing_time('test')


if __name__ == '__main__':
    main()
