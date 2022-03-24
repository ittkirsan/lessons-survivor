def SumOfThe(N, data):
    summa_min = 0
    summa_max = 0
    sum_of_all_numbers = 0
    for i in data:
        if i < 0:
            summa_min += i
        else:
            summa_max += i

    sum_of_all_numbers = summa_min + summa_max
    K = int(sum_of_all_numbers/2)

    return K


print(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90, ]))
