
def PatternUnlock(N, hits):
    ELEMENT_LIST_1 = [1, 8, 3, 5]
    ELEMENT_LIST_2 = [6, 2, 7, 4, 9]
    line_length_unlock = 0
    DIAGONAL_LENGTH = 2**0.5

    for i in range(N-1):
        if (hits[i] in ELEMENT_LIST_1 and hits[i+1] in ELEMENT_LIST_1):
            line_length_unlock = line_length_unlock + DIAGONAL_LENGTH
        elif (hits[i] in ELEMENT_LIST_2 and hits[i+1] in ELEMENT_LIST_2):
            line_length_unlock = line_length_unlock + DIAGONAL_LENGTH
        else:
            line_length_unlock += 1

    unlock_code_string = str(round(line_length_unlock, 5))
    unlock_code_string = unlock_code_string.replace('.', '')
    unlock_code_string = unlock_code_string.replace('0', '')

    return unlock_code_string
