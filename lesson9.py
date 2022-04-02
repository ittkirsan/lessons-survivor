def TheRabbitsFoot(s, encode):
    # encode = true (зашифровывает исходную строку)
    # encode = false (расшифровывает исходную строку)

    if encode == True:
        s = ''.join(s.split())
        sq = len(s)**(0.5)
        str1 = ''
        array = []
        decode_string = ''
        rows = int(sq)
        cols = round(sq)
        if len(s) > rows*cols:
            rows += 1

        for i in range(0, len(s), cols):
            str1 = str1 + (s[i:i+cols])
            array.append(str1)
            str1 = ''

        for i in range(cols):
            if i == len(array[rows - 1]) - 1:
                for j in range(rows):
                    decode_string += array[j][i]
                decode_string += ' '
            else:
                for j in range(rows-1):
                    decode_string += array[j][i]
                decode_string += ' '

        decode_string = decode_string.rstrip()

    else:

        s = s.split()
        array = []
        for elem in s:
            array.append(list(elem))
        decode_string = ''
        for i in range(len(array[0])):
            for j in array:
                if len(j) > i:
                    decode_string += j[i]
                else:
                    continue

    return decode_string
