
def WordSearch(N, s, subs):
    str1 = ''
    result = []
    searching_word_list = []

    l = list(s)

    while len(l) > N:
        count = 0
        for i in range(N, 0, -1):
            if l[i] == ' ':
                k = i
                count = 1
                for j in range(0, k+1):
                    str1 = str1 + l[0]
                    l.pop(0)
                result.append(str1)
                str1 = ''
                break
        if count == 0:
            for j in range(0, N):
                str1 = str1 + l[0]
                l.pop(0)
            result.append(str1)
            str1 = ''

    for m in range(len(l)):
        str1 = str1 + l[0]
        l.pop(0)
    result.append(str1)

    for strings in result:
        mark = 0
        for words in strings.split():
            if words == subs:
                mark = 1
        if mark == 1:
            searching_word_list.append(1)

        else:
            searching_word_list.append(0)

    return searching_word_list
