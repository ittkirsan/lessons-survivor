

def Football(F, N):
    ARRAY_IN_ASCEND = sorted(F)
    if N == 1:
        return False
    elif F == ARRAY_IN_ASCEND:
        return False
    count = 0

    for i in range(N):
        if F[i] != ARRAY_IN_ASCEND[i]:
            count += 1
            if count == 1:
                start = i

    if count == 2:
        return True
    elif count > 2:
        for k in range(N-1, 0, -1):
            if F[k] != ARRAY_IN_ASCEND[k]:
                end = k
                break

    F[start:end+1] = reversed(F[start:end+1])

    if ARRAY_IN_ASCEND == F:
        return True

    return False
