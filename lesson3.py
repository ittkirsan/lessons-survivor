def ConquestCampaign(N, M, L, battalion):

    if not isinstance(N, int) or N < 1:
        raise TypeError(f'Значение N не является числом или менее 1:{N}')
    elif not isinstance(M, int) or M < 1:
        raise TypeError(f'Значение M не является числом или менее 1:{M}')
    elif not isinstance(L, int) or L < 1:
        raise TypeError(f'Значение L не является числом или менее 1:{L}')
    elif not isinstance(battalion, list):
        raise TypeError(f'В battalion передан не массив:{battalion}')

    size_of_squares_state = [[0]*M for i in range(N)]

    days = 1

    for i in range(0, len(battalion), 2):
        k = battalion[i] - 1
        l = battalion[i+1] - 1
        size_of_squares_state[k][l] = 1

    b = [[1]*M for i in range(N)]
    while size_of_squares_state != b:
        c = [[size_of_squares_state[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if size_of_squares_state[i][j] == 1:
                    if j < M-1:
                        c[i][j+1] = 1
                    if j > 0:
                        c[i][j-1] = 1
                    if i < N-1:
                        c[i+1][j] = 1
                    if i > 0:
                        c[i-1][j] = 1
        size_of_squares_state = c
        days += 1

    size_of_squares_state = size_of_squares_state.clear()
    c = c.clear()

    return days
