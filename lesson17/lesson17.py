

def LineAnalysis(line):
    SYMBOL = '*'
    if (len(line) == 1 and line[0] == SYMBOL) or len(line) == 0:
        return True
    elif line[0] != SYMBOL or line[-1] != SYMBOL:
        return False

    else:
        subline = SYMBOL
        i = 1
        while line[i] != SYMBOL:
            subline += line[i]
            i += 1
        subline += SYMBOL

    for i in range(0, len(line)-1, len(subline)-1):
        for j in range(len(subline)):
            if subline[j] != line[j+i]:
                return False
    return True
