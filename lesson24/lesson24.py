
def MatrixTurn(Matrix, M, N, T):

    matrixList = [['*' for i in range(N)] for j in range(M)]
    for turn in range(T):
        k = 0
        count = 0
        while count < N*M:
            for i in range(k, M-k):
                for j in range(k, N-k):
                    if i == k and j == k and i < M-k-1:
                        matrixList[i][j] = Matrix[i+1][j]
                        count += 1
                    elif i == k and j > k:
                        matrixList[i][j] = Matrix[i][j-1]
                        count += 1
                    elif i > k and j == k and i < M-k-1:
                        matrixList[i][j] = Matrix[i+1][j]
                        count += 1
                    elif i > k and j == N-k-1 and i < M-k-1:
                        matrixList[i][j] = Matrix[i-1][j]
                        count += 1
                    elif i == M-k-1 and j == N-k-1:
                        matrixList[i][j] = Matrix[i-1][j]
                        count += 1
                    elif i == M-k-1 and j < N-k-1:
                        matrixList[i][j] = Matrix[i][j+1]
                        count += 1

            k += 1
        for l in range(M):
            Matrix[l] = ''.join(matrixList[l])

    return Matrix
