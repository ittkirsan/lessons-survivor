
"""
Сигналы НЛО

Британские учёные перехватили трафик переговоров двух НЛО, шпионящих за Землёй. 
Как выяснилось, сигналы первой НЛО передаются в восьмеричной системе счисления, 
а сигналы второй НЛО передаются в шестнадцатеричной системе счисления.
Для быстрой расшифровки их переговоры надо представить в более привычной землянам 
десятичной системе счисления. Срочно требуется конвертор для разных систем счисления.
Функция
int [] UFO(int N, int [] data, bool octal)
получает на вход длину N цифровой записи трафика, сам трафик (последовательность положительных чисел) 
в массиве data, и флажок octal, который задаёт систему счисления входных данных: 
восьмеричная если octal = true, и шестнадцатеричная в противном случае.
Если числа подаются в восьмеричной системе счисления, гарантируется, что в них не будет цифр 8 и 9.
Функция возвращает массив длины N, содержащий исходные числа, преобразованные в десятичную систему счисления.
Например, если на вход подаётся массив из двух чисел 1234,1777 с флажком octal = false, то результат будет 4660,6007.
А если флажок для данного массива будет true, то результат будет 668,1023.
"""


def UFO(N, data, octal):

    result = []
    if octal == True:

        for k in data:
            el = str(k)
            elstr = el.strip()
            len_el = len(elstr)-1
            base_8 = 0
            for i in elstr:
                base_8 += int(i) * (8**len_el)
                len_el -= 1
            result.append(base_8)

    else:
        for k in data:
            el = str(k)
            elstr = el.strip()
            len_el = len(elstr)-1
            base_16 = 0
            for i in elstr:
                base_16 += int(i) * (16**len_el)
                len_el -= 1
            result.append(base_16)

    return result


print(UFO(2, [1234, 1777], True))
print(UFO(2, [1234, 1777], False))
