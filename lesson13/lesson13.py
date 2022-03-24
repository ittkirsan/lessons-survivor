

def UFO(N, data, octal):

    array_of_numbers_in_decimal_system = []
    if octal == True:

        for k in data:
            el = str(k)
            elstr = el.strip()
            len_el = len(elstr)-1
            base_8 = 0
            for i in elstr:
                base_8 += int(i) * (8**len_el)
                len_el -= 1
            array_of_numbers_in_decimal_system.append(base_8)

    else:
        for k in data:
            el = str(k)
            elstr = el.strip()
            len_el = len(elstr)-1
            base_16 = 0
            for i in elstr:
                base_16 += int(i) * (16**len_el)
                len_el -= 1
            array_of_numbers_in_decimal_system.append(base_16)

    return array_of_numbers_in_decimal_system
