def squirrel(N):
    factorial = 1

    for i in range(2, N+1):
        factorial *= i

    k = str(factorial)
    amount_diamonds = int(k[0])

    return amount_diamonds
