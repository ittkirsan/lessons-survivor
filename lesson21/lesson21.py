
def BiggerGreater(string):
    k = len(string)-1
    for i in range(k, 0, -1):
        if string[i] > string[i-1]:

            string_new = list(string[i-1:])
            sortString = sorted(string_new)
            indx = sortString.index(string_new[0])
            elem = sortString[indx + 1]
            ind = string_new.index(elem)

            string_new[0], string_new[ind] = string_new[ind], string_new[0]
            result = string[:i-1] + \
                ''.join(string_new[0]) + ''.join(sorted(string_new[1:]))
            return result

    result = ''
    return result
