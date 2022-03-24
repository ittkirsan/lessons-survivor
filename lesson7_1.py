
def WordSearch(N, s, subs):
    str1 = ''
    result = []
    searching_word_list = []

    list_of_sting_symbols = list(s)

    while len(list_of_sting_symbols) > N:
        count = 0
        for i in range(N, 0, -1):
            if list_of_sting_symbols[i] == ' ':
                k = i
                count = 1
                for j in range(0, k+1):
                    str1 = str1 + list_of_sting_symbols[0]
                    list_of_sting_symbols.pop(0)
                result.append(str1)
                str1 = ''
                break
        if count == 0:
            for j in range(0, N):
                str1 = str1 + list_of_sting_symbols[0]
                list_of_sting_symbols.pop(0)
            result.append(str1)
            str1 = ''

    for m in range(len(list_of_sting_symbols)):
        str1 = str1 + list_of_sting_symbols[0]
        list_of_sting_symbols.pop(0)
    result.append(str1)

    for strings in result:
        word_in_string = 0
        for words in strings.split():
            if words == subs:
                word_in_string = 1
        if word_in_string == 1:
            searching_word_list.append(1)

        else:
            searching_word_list.append(0)

    return searching_word_list
