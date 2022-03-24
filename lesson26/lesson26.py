

def white_walkers(village):
    HUMAN = "1234567890"
    list_hum_ww = []
    list_humun = []

    for i in range(len(village)):
        if village[i] in HUMAN:
            list_hum_ww.append(village[i])
            list_humun.append(int(village[i]))

        elif village[i] == '=':
            list_hum_ww.append(village[i])

    sum_digits = 0
    count = 0

    for j in range(len(list_hum_ww)-4):
        if list_hum_ww[j] in HUMAN:
            sum_digits += int(list_hum_ww[j])
            if list_hum_ww[j+4] in HUMAN:
                sum_digits += int(list_hum_ww[j+4])
                if sum_digits == 10:
                    count += 1
            sum_digits = 0
    count_sum = 0
    for k in range(len(list_humun)-1):
        if list_humun[k] + list_humun[k+1] == 10:
            count_sum += 1

    if count == count_sum and count != 0:
        return True
    else:
        return False
