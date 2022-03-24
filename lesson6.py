
def PatternUnlock(N, hits):
    list1 = [1, 8, 3, 5]
    list2 = [6, 2, 7, 4, 9]
    line_length_unlock = 0

    for i in range(N-1):
        if (hits[i] in list1 and hits[i+1] in list1):
            line_length_unlock = line_length_unlock + 2**0.5
        elif (hits[i] in list2 and hits[i+1] in list2):
            line_length_unlock = line_length_unlock + 2**0.5
        else:
            line_length_unlock += 1

    unlock_code_string = str(round(line_length_unlock, 5))
    unlock_code_string = unlock_code_string.replace('.', '')
    unlock_code_string = unlock_code_string.replace('0', '')

    return unlock_code_string
