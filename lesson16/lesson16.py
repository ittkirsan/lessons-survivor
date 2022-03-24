
def MaximumDiscount(N, price):

    spisok = sorted(price, reverse=True)
    max_discont = 0

    for i in range(2, len(spisok), 3):
        max_discont += spisok[i]

    return max_discont
