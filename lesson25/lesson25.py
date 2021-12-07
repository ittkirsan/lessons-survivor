
def transform(A):

    result = []
    for i in range(0, len(A)):
        for j in range(0, len(A) - i):
            k = i + j
            ztikl = A[j:k + 1]
            ztikl = sorted(ztikl)
            if len(ztikl) != 0:
                result.append(ztikl[-1])
    return


""" основная функция"""


def TransformTransform(A, n):

    result = transform(transform(A))
    total = 0
    for i in result:
        total += i
    return True if total % 2 == 0 else False
