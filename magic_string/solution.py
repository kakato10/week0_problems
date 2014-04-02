def magic_string(string):
    step_count = 0
    for index in range(0, len(string) // 2):
        if string[index] != ">":
            step_count = step_count + 1
    for index in range(len(string) // 2, len(string)):
        if string[index] != "<":
            step_count = step_count + 1
    return step_count
