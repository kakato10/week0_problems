def reduce_file_path(path):
    if path == '/':
        return path
    path_split = path.split('/')
    for i in range(0, len(path_split)):
        if path_split[i] == '.':
            path_split[i] = ''
    for i in range(1, len(path_split)):
        if path_split[i] == '..':
            path_split[i] = ''
            path_split[i - 1] = ''
    for element in path_split:
        if element == '':
            path_split.remove(element)
    path = '/'
    for i in range(0, len(path_split)):
        if path_split[i] == '' or i == len(path_split) - 1:
            path = path + path_split[i]

        else:
            path = path + path_split[i] + '/'
    path_split = list(path)
    if path_split[len(path_split) - 1] == '/' and len(path_split) != 1:
        path = ''
        for i in range(0, len(path_split) - 1):
            path = path + path_split[i]
    else:
        path = ''.join(path_split)
    return path
