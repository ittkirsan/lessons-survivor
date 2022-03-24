

def Keymaker(k):
    NUMBER_OF_DOORS = k
    doors_list = [0] * NUMBER_OF_DOORS

    for i in range(NUMBER_OF_DOORS):
        if i == 0:
            for x in range(NUMBER_OF_DOORS):
                doors_list[x] = 1

        elif i == 1:
            for x in range(i, NUMBER_OF_DOORS, 2):
                doors_list[x] = 0

        else:
            for x in range(i, NUMBER_OF_DOORS, i+1):
                if doors_list[x] == 0:
                    doors_list[x] = 1
                else:
                    doors_list[x] = 0

    doors_string = ''.join([str(x) for x in doors_list])

    return doors_string
