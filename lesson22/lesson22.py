

def SherlockValidString(string):
    # создаем список элементов которые встречаются строке
    unik = []
    for i in string:
        if i not in unik:
            unik.append(i)
    unik = ''.join(unik)
    # считаем колличесто вхождений каждой уникальной буквы
    countLetter = []
    for i in range(len(unik)):
        if unik[i] in string:
            countLetter.append(string.count(unik[i]))
    # проеряем валидность пароля
    countLetter = sorted(countLetter)
    if countLetter[0] == 1:
        countLetter.pop(0)
    if len(countLetter) < 1:
        return True
    elif len(countLetter) == countLetter.count(countLetter[0]):
        return True
    else:
        countLetter[len(countLetter)-1] = countLetter[len(countLetter)-1]-1
        if len(countLetter) == countLetter.count(countLetter[0]):
            return True
        else:
            return False
