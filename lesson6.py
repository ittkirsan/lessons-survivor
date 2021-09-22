
def PatternUnlock(N, hits):
    list1 = [1, 8, 3, 5]
    list2 = [6, 2, 7, 4, 9]
    summa = 0

    for i in range(N-1):
        if (hits[i] in list1 and hits[i+1] in list1):
            summa = summa + 2**0.5
        elif (hits[i] in list2 and hits[i+1] in list2):
            summa = summa + 2**0.5
        else:
            summa += 1

    result = str(round(summa, 5))
    result = result.replace('.', '')
    result = result.replace('0', '')

    return result
