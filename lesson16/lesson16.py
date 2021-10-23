
def MaximumDiscount(N, price):

    spisok = sorted(price, reverse=True)
    discont = 0

    for i in range(2, len(spisok), 3):
        discont += spisok[i]

    return discont
