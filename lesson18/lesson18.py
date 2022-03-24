

def MisterRobot(N: int, data: int):
    ETALON = sorted(data)
    for k in range(N-1):
        for i in range(N, 2, -1):
            if data[i-1] == data and data[i-3] < data[i-2][i-2] + 1 and data[i-3] == data[i-2] + 1:
                break
            elif data[i-3] < data[i-2] and data[i-3] < data[i-1]:
                continue

            else:
                for j in range(3):
                    if (data[i-3] > data[i-2]) or (data[i-3] > data[i-1]):
                        data[i-1], data[i-2], data[i -
                                                   3] = data[i-3], data[i-1], data[i-2]
                    else:
                        break
    if data == ETALON:
        return True
    else:
        return False
