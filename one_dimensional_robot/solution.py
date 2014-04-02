def final_position(commands, left, right):
    current_postion = 0
    for command in commands:
        if command == 'R' and current_postion + 1 <= right:
            current_postion = current_postion + 1
        if command == 'L' and current_postion - 1 >= (- 1) * left:
            current_postion = current_postion - 1
    return current_postion
