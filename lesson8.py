def SumOfThe(N, data):
    summa_min = 0
    summa_max = 0
    summ = 0
    for i in data:
        if i < 0:
            summa_min += i
        else:
            summa_max += i

    summ = summa_min + summa_max
    K = int(summ/2)

    return K
