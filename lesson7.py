
def WordSearch(N, s, subs):
    result = []
    result_list = []

    l = s.split()
    str1 = ''
    strlen = 0

    for (index, elem) in enumerate(l):
        strlen += len(l[index])
        if strlen == N:
            str1 = str1 + l[index]
            strlen = 0
            result.append(str1)
            str1 = ''

        elif strlen > N:
            result.append(str1)
            str1 = ''
            str2 = ''
            if len(l[index]) == N:
                str1 = str1 + l[index]
                result.append(str1)
                strlen = 0
                str1 = ''

            elif index == len(l)-1 and len(l[index]) <= N:
                str1 = str1 + l[index]
                result.append(str1)

            elif len(l[index]) < N:
                str1 = str1 + l[index] + ' '
                strlen = len(l[index]) + 1

            else:
                str2 = elem[0:N]
                result.append(str2)
                str1 = str1 + elem[N:] + ' '
                strlen = (len(l[index]) - N) + 1

        # elif index == len(l)-1:
            # str1 = str1 + l[index]
            # result.append(str1)

        else:
            str1 = str1 + l[index] + " "
            strlen += 1

    for strings in result:
        mark = 0
        for words in strings.split():
            if words == subs:
                mark = 1
        if mark == 1:
            result_list.append(1)

        else:
            result_list.append(0)

    return result_list


#print(WordSearch(10, '12345', 'subs'))
print(WordSearch(9, '1) stroka razbivaetsya na nabor strok...', 'strok'))
print(WordSearch(12, 'строкаразбивается на набор строк через выравнивание по заданной ширине.', 'строк'))
