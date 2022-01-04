


def TankRush(H1, W1, S1,  H2, W2, S2):

    array_map = S1.split()
    array_tank = S2.split()
    # ищем вхожение первого символа
    for i in range(H1):
        if H1 - i >= H2:
            for j in range(W1):
                if W1 - j >= W2:
                    if array_map[i][j] == array_tank[0][0]:
                        count = 0
                    # если есть вхождение проверяем вхождение самой матрицы
                        for k in range(H2):
                            for m in range(W2):
                                if array_map[i + k][j + m] == array_tank[k][m]:
                                    count += 1
                                else:
                                    break
                                if count == H2*W2:
                                    return True

    return False
