def squirrel(N):
    factorial = 1

    for i in range(2, N+1):
        factorial *= i

    k = str(factorial)
    izu = int(k[0])

    return izu
