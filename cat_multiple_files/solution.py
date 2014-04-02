def main(name1, name2):
    content = ''
    filename = name1
    file = open(filename, 'r')
    content = file.read() + '\n\n'
    file.close()
    filename = name2
    file = open(filename, 'r')
    content = content + file.read()
    file.close()
    return content
