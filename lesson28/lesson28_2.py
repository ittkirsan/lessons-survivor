def Keymaker(k):

    if k == 1:
        return '1'

    doors = [0] * k
    for i in range(1, k):
        if i**2 <= k:
            doors[(i**2)-1] = 1
        else:
            break

    return ''.join([str(x) for x in doors])
