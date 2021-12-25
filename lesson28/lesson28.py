

def Keymaker(k):

    doors = [0] * k

    for i in range(k):
        if i == 0:
            for x in range(k):
                doors[x] = 1

        elif i == 1:
            for x in range(i, k, 2):
                doors[x] = 0

        else:
            for x in range(i, k, i+1):
                if doors[x] == 0:
                    doors[x] = 1
                else:
                    doors[x] = 0

    doors_string = ''.join([str(x) for x in doors])

    return doors_string
