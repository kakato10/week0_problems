from time import time
from datetime import datetime


def main():
    list_to_display = []
    orders = {}
    temp = True
    saves_names = []
    save = {}
    print ('---------------------------------------')
    print ('            START              ')
    print ('---------------------------------------')
    print('Type "take <name> <value>" to make an order.')
    print('Type "status" to see all your order.')
    print('Type "save" to save your current order.')
    print('Type "list" to see all saved orders.')
    print('Type "load <number_of_save>" to open a saved order.')
    print('Type "finish" to confirm the order')
    while temp:

        command = input("Enter command>")
        if command == 'finish':
            print ('Thanks for the order!')
            temp = False

        elif command[0:4] == 'take':
            t = 0
            name = ''
            for i in range(5, len(command)):
                if command[i] == ' ':
                    t = i
                    break
            name = command[5:t]
            if name not in orders:
                orders[name] = float(command[t + 1: len(command)])
            else:
                orders[name] = orders[name] + float(command[t + 1: len(command)])
            print ('Taking order from ' + name + ' for ' + command[t + 1: len(command)])
            list_of_orders = []
            for i in orders:
                list_of_orders.append(i + ' - ' + str(orders[i]))
        elif command == 'status':
            for order in list_of_orders:
                print (order)

        elif command == 'save':
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            filename = str(stamp) + '.txt'
            file = open(filename, 'w')
            file.write('\n'.join(list_of_orders))
            file.close()
            filename = filename
            saves_names.append(filename)
            for i in range(0, len(saves_names)):
                save[str(i + 1)] = saves_names[i]
            print("Order saved!")

        elif command == "list":
            if len(save) == 1:
                print("The order you already saved is:")
            else:
                print("The orders you already saved are:")
            for i in save:
                if '[' + i + ']' + ' - ' + save[i] not in list_to_display:
                    list_to_display.append('[' + i + ']' + ' - ' + save[i])
            list_to_display.sort()
            for i in list_to_display:
                print (i)

        elif command[0:4] == 'load':
            if len(command) < 6:
                print ("Bad input!")
            else:
                filename = save[(str(int(command[5: len(command)])))]
                file = open(filename, 'r')
                content = file.read()
                orders = {}
                sep_content = []
                p = 0
                for i in range(0, len(content)):
                    if content[i] == '\n':
                        sep_content.append(content[p:i])
                        p = i + 1
                        i = i + 1
                    if i == len(content) - 1:
                        sep_content.append(content[p: i + 1])
                        break
                for i in sep_content:
                    for j in range(0, len(i)):
                        if i[j] == ' ':
                            orders[i[0: j]] = i[j + 3:]
                            break
                list_of_orders = []
                for i in orders:
                    list_of_orders.append(i + ' - ' + str(orders[i]))
                print("You have loaded: " + save[(str(int(command[5: len(command)])))])
        else:
            print ("Bad input!")

if __name__ == '__main__':
    main()
