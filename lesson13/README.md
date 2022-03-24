
## Сигналы НЛО

Британские учёные перехватили трафик переговоров двух НЛО, шпионящих за Землёй. 
Как выяснилось, сигналы первой НЛО передаются в восьмеричной системе счисления, 
а сигналы второй НЛО передаются в шестнадцатеричной системе счисления.
Для быстрой расшифровки их переговоры надо представить в более привычной землянам 
десятичной системе счисления. Срочно требуется конвертор для разных систем счисления.
____

## Функция

*int [] UFO(int N, int [] data, bool octal)*

получает на вход длину N цифровой записи трафика, сам трафик (последовательность положительных чисел) 
в массиве data, и флажок octal, который задаёт систему счисления входных данных: 
восьмеричная если octal = true, и шестнадцатеричная в противном случае.
Если числа подаются в восьмеричной системе счисления, гарантируется, что в них не будет цифр 8 и 9.
Функция возвращает массив длины N, содержащий исходные числа, преобразованные в десятичную систему счисления.
Например, если на вход подаётся массив из двух чисел 1234,1777 с флажком octal = false, то результат будет 4660,6007.
А если флажок для данного массива будет true, то результат будет 668,1023.