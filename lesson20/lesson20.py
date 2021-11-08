list_string = []  # список строк для операций 1 и 2
undo = []  # список для отмененых операций
flag = True


def BastShoe(command):
    global list_string, undo, flag

    # разбиваем входящую строку на номер команды и аргументы
    command = command.split(' ', maxsplit=1)
    # выполняем операцию 1
    if command[0] == '1':
        if len(undo) > 0:  # для прекращения цепочки для операции 4
            undo.clear()
            flag = False
        elif len(undo) == 0:
            flag = True
        if len(list_string) == 0:
            list_string.append(command[1])
            return list_string[0]
        else:
            list_string.append(list_string[-1] + command[1])
        return list_string[len(list_string)-1]

    # выполняем операцию 2
    elif command[0] == '2':
        if len(undo) > 0:
            undo.clear()
            flag = False
        elif len(undo) == 0:
            flag = True
        if len(list_string) == 0:
            return ''
        elif len(list_string[-1]) >= int(command[1]):
            list_string.append(list_string[-1][:-int(command[1])])
            return list_string[-1]
        else:
            list_string.append('')
            return list_string[-1]

    # выполняем операцию 3
    elif command[0] == '3':
        if int(command[1]) >= len(list_string[-1]):
            return ''
        else:
            return list_string[-1][int(command[1])]

    # выполняем операцию 4
    elif command[0] == '4':
        if len(list_string) == 0:
            return ""
        elif flag == False and len(undo) == 0:
            undo.append(list_string[-1])
            list_string.pop()
            return list_string[-1]
        elif flag == False and len(undo) != 0:
            return list_string[-1]

        else:
            undo.append(list_string[-1])
            list_string.pop()
            if len(list_string) == 0:
                return ''
            else:
                return list_string[-1]

    # выполняем операцию 5
    elif command[0] == "5":
        if len(undo) == 0:
            return list_string[-1]
        elif len(undo) > 0:
            list_string.append(undo[-1])
            undo.pop()
            return list_string[-1]
    # в других случаях
    else:
        if len(list_string) > 0:
            return list_string[-1]
        else:
            return ""
