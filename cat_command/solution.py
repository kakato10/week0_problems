# cat.py
def main(name):
    content = ''
    filename = name
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content
