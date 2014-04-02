import sys
import glob


def main():
    contents = []
    if len(sys.argv) > 1:
        for file_name in sys.argv:
            if file_name != sys.argv[0]:
                file = open(file_name, 'r')
                contents.append(file.read())
                file.close()

    else:
        print ("No arguements given")
    list_of_files = glob.glob("*.txt")
    filename2 = 'MEGATRON.txt'
    if filename2 not in list_of_files:
        file1 = open(filename2, 'w')
        file1.write('\n'.join(contents))
    else:
        file1 = open(filename2, 'a')
        file1.write('\n' + '\n'.join(contents))
    file1.close()

if __name__ == '__main__':
    main()
