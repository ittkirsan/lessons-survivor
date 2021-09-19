def ConquestCampaign(N, M, L, battalion):

    a = [[0]*M for i in range(N)]
    b = [[1]*M for i in range(N)]
    days = 1

    for i in range(0, len(battalion), 2):
        k = battalion[i] - 1
        l = battalion[i+1] - 1
        a[k][l] = 1

    while a != b:
        c = [[a[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if a[i][j] == 1:
                    if j < M-1:
                        b[i][j+1] = 1
                    if j > 0:
                        b[i][j-1] = 1
                    if i < N-1:
                        b[i+1][j] = 1
                    if i > 0:
                        b[i-1][j] = 1
    a = c
    days += 1
    return days
