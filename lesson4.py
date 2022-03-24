

def MadMax(N, Tele):
    Tele.sort()
    result_impuls_array = []

    for i in range(N-1):
        if i < (N-1)/2:
            result_impuls_array.append(Tele[i])

    for i in range(N-1, -1, -1):
        if i >= (N-1)/2:
            result_impuls_array.append(Tele[i])

    return result_impuls_array
