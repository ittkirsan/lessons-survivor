

def BigMinus(s1, s2):

    if not isinstance(s1, str):
        raise TypeError(f'Значение s1 не является строковым типом:{s1}')
    elif not isinstance(s2, str):
        raise TypeError(f'Значение s2 не является строковым типом:{s2}')

    if len(s1) == len(s2):
        for i in range(len(s1)):
            if int(s1[i]) > int(s2[i]):
                s_max = s1
                s_min = s2
                break
            else:
                s_min = s1
                s_max = s2
                break

    elif len(s1) < len(s2):
        s_min = s1
        s_max = s2
    else:
        s_max = s1
        s_min = s2
    N1 = len(s_max)
    N2 = len(s_min)

    nst = ""
    k = 1

    mark = 0

    for i in range((N1 - 1), -1, -1):

        el = int(s_max[i]) - mark

        if k <= N2:
            el = el - int(s_min[N2 - k])
            if el < 0:
                el = 10 + el
                nst += str(el)
                k += 1
                mark = 1

            else:
                nst += str(el)
                k += 1
                mark = 0

        elif k > N2 and el >= 0:
            nst += str(el)
            mark = 0

        elif k > N2 and el < 0:
            el = 10 + el
            nst += str(el)
            mark = 1

    result = nst[::-1]
    for i in range(len(result)-1):
        if int(result[0]) == 0:
            result = result[1:]

    nst = "***ERROR***"

    return result
