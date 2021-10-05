def TheRabbitsFoot(s, encode):
    if encode == True:
        s = ''.join(s.split())
        sq = len(s)**(0.5)
        str1 = ''
        array = []
        result_str = ''
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
                    result_str += array[j][i]
                result_str += ' '
            else:
                for j in range(rows-1):
                    result_str += array[j][i]
                result_str += ' '

        result_str = result_str.rstrip()

    else:

        s = s.split()
        array = []
        for elem in s:
            array.append(list(elem))
        result_str = ''
        for i in range(len(array[0])):
            for j in array:
                if len(j) > i:
                    result_str += j[i]
                else:
                    continue

    return result_str
