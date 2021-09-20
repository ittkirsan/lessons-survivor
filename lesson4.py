

def MadMax(N, Tele):
    Tele.sort()
    Tele2 = []

    for i in range(N-1):
        if i < (N-1)/2:
            Tele2.append(Tele[i])

    for i in range(N-1, -1, -1):
        if i >= (N-1)/2:
            Tele2.append(Tele[i])

    return Tele2
