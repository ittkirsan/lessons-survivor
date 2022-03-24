

def Keymaker(k):

    doors_list = [0] * k

    for i in range(k):
        if i == 0:
            for x in range(k):
                doors_list[x] = 1

        elif i == 1:
            for x in range(i, k, 2):
                doors_list[x] = 0

        else:
            for x in range(i, k, i+1):
                if doors_list[x] == 0:
                    doors_list[x] = 1
                else:
                    doors_list[x] = 0

    doors_string = ''.join([str(x) for x in doors_list])

    return doors_string
