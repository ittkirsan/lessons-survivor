list_string = []  # список строк для операций 1 и 2
undo = []  # список для отмененых операций
flag = 0


def BastShoe(command):
    global flag, list_string, undo
    ADD_TO_END = '1'  # добавить в конец строки
    DEL_SYMBOLS = '2'  # удалить символы
    GET_SYNBOL = '3'  # выдать символ
    UNDO = '4'  # отмена последней операции ADD_TO_END или DEL_SYMBOLS
    REDO = '5'  # выполнить заново последнюю отменённую с помощью Undo операцию

    # разбиваем входящую строку на номер команды и аргументы
    command = command.split(' ', maxsplit=1)
    # выполняем операцию 1
    if command[1] == ADD_TO_END:
        if len(undo) > 0:  # для прекращения цепочки для операции 4
            undo.clear()
            del list_string[:-1]
            flag = -1
        if len(list_string) == 0:
            list_string.append(command[1])
            flag += 1
            return list_string[0]
        else:
            list_string.append(list_string[-1] + command[1])
            flag += 1
            return list_string[len(list_string)-1]

    # выполняем операцию 2
    elif command[0] == DEL_SYMBOLS:
        if len(undo) > 0:
            undo.clear()
            list_string.append('')
            del list_string[:-1]
            flag = -1
        else:
            undo.append('')

        if len(list_string[-1]) >= int(command[1]):
            list_string.append(list_string[-1][:-int(command[1])])
            flag += 1
            return list_string[-1]
        else:
            flag += 1
            return ''

    # выполняем операцию 3
    elif command[0] == GET_SYNBOL:
        if int(command[1]) >= len(list_string[-1]):
            return ''
        else:
            return list_string[-1][int(command[1])]

    # выполняем операцию 4
    elif command[0] == UNDO:
        if len(list_string) == 0:
            return ""
        elif flag > 0:
            undo.append(list_string[-1])
            list_string.pop()
            flag -= 1
            if len(list_string) == 0:
                return ""
            else:
                return list_string[-1]
        elif flag <= 0:
            return list_string[0]

            # выполняем операцию 5
    elif command[0] == REDO:
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
