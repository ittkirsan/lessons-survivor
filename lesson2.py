
def odometer(oksana):
    S = 0
    time = 0
    if len(oksana) % 2 == 0:
        mas = len(oksana)
    else:
        mas = len(oksana) - 1

    for i in range(1, mas, 2):
        S = S + oksana[i-1] * (oksana[i]-time)
        time = oksana[i]

    return S
