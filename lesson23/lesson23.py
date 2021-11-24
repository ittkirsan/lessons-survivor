

def TreeOfLife(H, W, N, tree):
    treeList = []
    result = []

    for i in range(H):
        a = []
        for j in range(W):
            if tree[i][j] == ".":
                a.append(0)
            else:
                a.append(1)
        treeList.append(a)

    for year in range(0, N):
        for i in range(0, H):
            for j in range(0, W):
                treeList[i][j] += 1
        if year % 2 != 0:
            for k in range(H):
                for l in range(W):
                    if treeList[k][l] > 2:
                        if k - 1 >= 0 and treeList[k - 1][l] < 3:
                            treeList[k - 1][l] = 0
                        if k + 1 < H and treeList[k + 1][l] < 3:
                            treeList[k + 1][l] = 0
                        if l - 1 >= 0 and treeList[k][l - 1] < 3:
                            treeList[k][l - 1] = 0
                        if l + 1 < W and treeList[k][l + 1] < 3:
                            treeList[k][l + 1] = 0
                        treeList[k][l] = 0

    for row in treeList:
        newstr = ''
        for j in row:
            if j == 0:
                newstr += '.'
            else:
                newstr += '+'
        result.append(newstr)

    return result
