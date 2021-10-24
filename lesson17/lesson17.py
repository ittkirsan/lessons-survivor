

def LineAnalysis(line):

    if (len(line) == 1 and line[0] == '*') or len(line) == 0:
        return True
    elif line[0] != '*' or line[-1] != '*':
        return False

    else:
        subline = '*'
        i = 1
        while line[i] != '*':
            subline += line[i]
            i += 1
        subline += '*'

    for i in range(0, len(line)-1, len(subline)-1):
        for j in range(len(subline)):
            if subline[j] != line[j+i]:
                return False
    return True
