def SumOfThe(N, data):
    sum_of_negative_numbers = 0
    sum_of_positive_numbers = 0
    sum_of_all_numbers = 0
    for i in data:
        if i < 0:
            sum_of_negative_numbers += i
        else:
            sum_of_positive_numbers += i

    sum_of_all_numbers = sum_of_negative_numbers + sum_of_positive_numbers
    sum_of_all_numbers_in_summary = int(sum_of_all_numbers/2)

    return sum_of_all_numbers_in_summary


print(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90, ]))
