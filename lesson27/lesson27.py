

def Football(F, N):
    F_sort = sorted(F)
    if F == F_sort:
        return True
    count = 0

    for i in range(N):
        if F[i] != F_sort[i]:
            count += 1
            if count == 1:
                start = i

    if count == 2:
        return True
    elif count > 2:
        for k in range(N-1, 0, -1):
            if F[k] != F_sort[k]:
                end = k
                break

    F[start:end+1] = reversed(F[start:end+1])

    if F_sort == F:
        return True

    return False
